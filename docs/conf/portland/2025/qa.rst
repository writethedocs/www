:template: {{year}}/generic.html
:og:image: _static/conf/images/headers/{{shortcode}}-{{year}}-opengraph.png

Speaker Q&A
===========

This page allows you to ask questions of our speakers,
and to vote on questions that you would like to see answered.
Refresh this page on the day of the conference talks to see them!

{% if qa %}
.. raw:: html

    <iframe src="https://app.sli.do/event/{{qa.event_id}}" height="100%" width="100%" frameBorder="0" style="min-height: 560px;" allow="clipboard-write" title="Slido"></iframe>

You can also use this link: https://app.sli.do/event/{{qa.event_id}}
{% else %}
Q&A details will be available closer to the conference date.
{% endif %}

If you experience technical issues, please report them in the #wtd-conferences channel on Slack.



