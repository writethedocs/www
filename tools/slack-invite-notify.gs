/**
 * Slack invite notifier — Google Apps Script.
 *
 * Posts each new Google Form submission to a Slack incoming webhook so a
 * moderator can manually invite the submitter. The form's response sheet
 * stays private; the submission data never leaves Google's infrastructure
 * except for the single webhook POST to Slack.
 *
 * Setup (one-time):
 *   1. Open the Google Form, click the three-dot menu > "Script editor"
 *      (this binds a new Apps Script project to the form).
 *   2. Replace the contents of Code.gs with this file.
 *   3. Project Settings (gear icon) > Script Properties > Add property:
 *         SLACK_WEBHOOK_URL  <slack-incoming-webhook-url>
 *   4. Triggers (clock icon) > Add Trigger:
 *         Function:        onFormSubmit
 *         Event source:    From form
 *         Event type:      On form submit
 *   5. Authorize the script when prompted (needs UrlFetch + form read).
 *   6. Submit a test response and confirm the moderator channel pings.
 *
 * This file lives in the repo for review/version-control only; Apps Script
 * does not auto-sync from here. If you change it, paste the new version
 * into the bound script project. (Or wire up `clasp` if that becomes
 * tedious — overkill for now.)
 */

function onFormSubmit(e) {
  var webhookUrl = PropertiesService.getScriptProperties().getProperty('SLACK_WEBHOOK_URL');
  if (!webhookUrl) {
    throw new Error('SLACK_WEBHOOK_URL is not set in Script Properties');
  }

  var fields = {};
  e.response.getItemResponses().forEach(function (ir) {
    fields[ir.getItem().getTitle()] = ir.getResponse();
  });

  var name = pickField(fields, ['Name', 'Full name', 'Your name']) || '(no name)';
  var email = pickField(fields, ['Email', 'Email address', 'Your email'])
    || e.response.getRespondentEmail()
    || '(no email)';

  var lines = [
    ':wave: New Slack invite request',
    '*Name:* ' + name,
    '*Email:* ' + email
  ];
  Object.keys(fields).forEach(function (key) {
    var lower = key.toLowerCase();
    if (lower === 'name' || lower === 'full name' || lower === 'your name') return;
    if (lower === 'email' || lower === 'email address' || lower === 'your email') return;
    if (!fields[key]) return;
    lines.push('*' + key + ':* ' + fields[key]);
  });

  var resp = UrlFetchApp.fetch(webhookUrl, {
    method: 'post',
    contentType: 'application/json',
    payload: JSON.stringify({ text: lines.join('\n') }),
    muteHttpExceptions: true
  });
  var code = resp.getResponseCode();
  if (code >= 300) {
    throw new Error('Slack webhook returned HTTP ' + code + ': ' + resp.getContentText());
  }
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
