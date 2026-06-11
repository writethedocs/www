/**
 * Slack invite notifier — Google Apps Script (batched digest).
 *
 * Posts a digest of new Google Form submissions to a Slack incoming webhook
 * on whatever schedule you pick (hourly, daily, etc.) so a moderator can
 * manually invite the submitters. The form's response sheet stays private;
 * the submission data never leaves Google's infrastructure except for the
 * single webhook POST per run.
 *
 * Setup (one-time):
 *   1. Open the Google Form, click the three-dot menu > "Script editor"
 *      (this binds a new Apps Script project to the form).
 *   2. Replace the contents of Code.gs with this file.
 *   3. Project Settings (gear icon) > Script Properties > Add property:
 *         SLACK_WEBHOOK_URL  <slack-incoming-webhook-url>
 *   4. Triggers (clock icon) > Add Trigger:
 *         Function:        notifyPendingSubmissions
 *         Event source:    Time-driven
 *         Type:            (pick — e.g. Hour timer, every hour;
 *                                  or Day timer, 9am-10am)
 *   5. Authorize the script when prompted (needs UrlFetch + form read).
 *   6. Run `notifyPendingSubmissions` once manually to seed the
 *      last-processed timestamp so existing submissions don't re-send.
 *      (Or run `markAllProcessed` to skip the historical backfill.)
 *
 * This file lives in the repo for review/version-control only; Apps Script
 * does not auto-sync from here. If you change it, paste the new version
 * into the bound script project. (Or wire up `clasp` if that becomes
 * tedious — overkill for now.)
 */

var LAST_PROCESSED_KEY = 'LAST_PROCESSED_TIMESTAMP';

function notifyPendingSubmissions() {
  var props = PropertiesService.getScriptProperties();
  var webhookUrl = props.getProperty('SLACK_WEBHOOK_URL');
  if (!webhookUrl) {
    throw new Error('SLACK_WEBHOOK_URL is not set in Script Properties');
  }

  var lastProcessed = parseTimestamp(props.getProperty(LAST_PROCESSED_KEY));
  var responses = FormApp.getActiveForm().getResponses();
  var pending = responses.filter(function (r) {
    return r.getTimestamp().getTime() > lastProcessed;
  });
  if (pending.length === 0) {
    return;
  }
  pending.sort(function (a, b) { return a.getTimestamp() - b.getTimestamp(); });

  var blocks = pending.map(formatResponse);
  var headerLine = pending.length === 1
    ? ':wave: 1 new Slack invite request'
    : ':wave: ' + pending.length + ' new Slack invite requests';
  var text = headerLine + '\n\n' + blocks.join('\n\n———\n\n');

  postToSlack(webhookUrl, text);

  var newest = pending[pending.length - 1].getTimestamp().getTime();
  props.setProperty(LAST_PROCESSED_KEY, String(newest));
}

function markAllProcessed() {
  var responses = FormApp.getActiveForm().getResponses();
  if (responses.length === 0) {
    PropertiesService.getScriptProperties().setProperty(LAST_PROCESSED_KEY, '0');
    return;
  }
  var newest = responses.reduce(function (acc, r) {
    var t = r.getTimestamp().getTime();
    return t > acc ? t : acc;
  }, 0);
  PropertiesService.getScriptProperties().setProperty(LAST_PROCESSED_KEY, String(newest));
}

function formatResponse(response) {
  var fields = {};
  response.getItemResponses().forEach(function (ir) {
    fields[ir.getItem().getTitle()] = ir.getResponse();
  });

  var name = pickField(fields, ['Name', 'Full name', 'Your name']) || '(no name)';
  var email = pickField(fields, ['Email', 'Email address', 'Your email'])
    || response.getRespondentEmail()
    || '(no email)';

  var lines = ['*Name:* ' + name, '*Email:* ' + email];
  Object.keys(fields).forEach(function (key) {
    var lower = key.toLowerCase();
    if (lower === 'name' || lower === 'full name' || lower === 'your name') return;
    if (lower === 'email' || lower === 'email address' || lower === 'your email') return;
    if (!fields[key]) return;
    lines.push('*' + key + ':* ' + fields[key]);
  });
  return lines.join('\n');
}

function pickField(fields, candidates) {
  var lowerMap = {};
  Object.keys(fields).forEach(function (k) { lowerMap[k.toLowerCase()] = fields[k]; });
  for (var i = 0; i < candidates.length; i++) {
    var v = lowerMap[candidates[i].toLowerCase()];
    if (v) return v;
  }
  return null;
}

function parseTimestamp(raw) {
  var n = raw ? parseInt(raw, 10) : 0;
  return isNaN(n) ? 0 : n;
}

function postToSlack(webhookUrl, text) {
  var resp = UrlFetchApp.fetch(webhookUrl, {
    method: 'post',
    contentType: 'application/json',
    payload: JSON.stringify({ text: text }),
    muteHttpExceptions: true
  });
  var code = resp.getResponseCode();
  if (code >= 300) {
    throw new Error('Slack webhook returned HTTP ' + code + ': ' + resp.getContentText());
  }
}
