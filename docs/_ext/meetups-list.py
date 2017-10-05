import meetup.api

client = meetup.api.Client('66f781546e532a32232d67507d6265')

event_info = client.GetEvents({'group_urlname': 'Write-The-Docs-YFC-Fredericton'})

event_info.__dict__
