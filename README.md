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

## How to run Atta on your local machine:
### Step 1
Execute `flask --app server.py run` in root directory to start up the Flask server.

### Step 2
You'll need to expose your localhost through a secure thirdparty method. I recommend using
`nGrok`

Once you have an `nGrok` account (don't worry, it's free for testing purposes), open a new 
terminal window and run `ngrok http http://localhost:8080`. Note: Your exact URL port may
be different. For instance, when I start the flask server, my port is 5000. So I would 
use `ngrok http http://localhost:5000`. 

### Step 3
Because setting up and installing an actual Slack App requires a paid workspace, and the app
currently isn't distributed, you will need to mimick calls being emmitted from the Slack API
Webhook by sending them yourself. 

You will need to POST to the endpoint `/events`, using the URL provided to you in the `Forwarding` field shown after launching
`nGrok`. Yours will be differnt, but it shuld look somnething like this `https://9f67-2603-9000-9400-3f6b-753c-8e99-213-c66e.ngrok-free.app/events`. 
Make sure to use the header `Content_Type: application/json` and the below JSON structure. For demonstration purposes,
I recommend simply copying and pasting the below object into the body of your call. The posted value comes from `message.text`, if you want to modify the message: 

```{"token": "EwzIcqOou7dXLzRFVjRB1vO8", "team_id": "T062WBK1PQ8", "api_app_id": "A07573Y0LKE", "event": {"user": "U06278YQZ3M", "type": "app_mention", "ts": "1717874918.920999", "client_msg_id": "2d393d81-71b9-4ca8-89e7-0bcaa1c56654", "text": "<@U075UUV4ZR6> WHAT AN APP WHAT AN APP WHAT A MIGHTY FINE APP. YES IT IS.", "team": "T062WBK1PQ8", "blocks": [{"type": "rich_text", "block_id": "rvYn4", "elements": [{"type": "rich_text_section", "elements": [{"type": "user", "user_id": "U075UUV4ZR6"}, {"type": "text", "text": " WHAT AN APP WHAT AN APP WHAT A MIGHTY FINE APP. YES IT IS."}]}]}], "channel": "C0758KKAF3N", "event_ts": "1717874918.920999"}, "type": "event_callback", "event_id": "Ev077A9EAZNG", "event_time": 1717874918, "authorizations": [{"enterprise_id": null, "team_id": "T062WBK1PQ8", "user_id": "U075UUV4ZR6", "is_bot": true, "is_enterprise_install": false}], "is_ext_shared_channel": false, "event_context": "4-eyJldCI6ImFwcF9tZW50aW9uIiwidGlkIjoiVDA2MldCSzFQUTgiLCJhaWQiOiJBMDc1NzNZMExLRSIsImNpZCI6IkMwNzU4S0tBRjNOIn0"}```

## Step 4
You can view the text in your browser by going to the `/` endpoint, again using the `Forwarding` URL from your `ngrok` launch.  
