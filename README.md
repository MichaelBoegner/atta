# Atta: A Slack-API Events ingestor to store evidence of your best work from Slack. 
## What is Atta?
Atta is a way to store important/performance-review-worthy Slack messages for future review 
or retrieval when prepping for a performance review. 

## Trello Board of Progress:
https://trello.com/b/RJnMt9Ba/atta-project

## What does the current version do? 
Currently, the app is:
- Catching a call emitted from Slack's API
- Publicizing my localhost through nGrok
- Catching those calls using an endpoint built with Flask 
- Mutating the received data to fit a newly created table in PostgreSQL 
- Displaying that table on a static HTML page, accessible through an nGrok proxied endpoint.

