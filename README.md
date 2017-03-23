# facebook-bot
Bot(skeleton) for your Facebook page messages


Need https for using facebook graph api. So if you are using local development server, install ngrok.
Usage :
  ngrok http 5000
Then note down the address. It will look something like this "https://ac433506.ngrok.io"


Create a Facebook app with category as "Apps for pages".
Then click "Add products" and add "Messenger".
Select your page from dropdown and generate the access token. Note down the access token. You will need to provide it in "server.py".
Click "Setup webhooks". Add address obtained from ngrok as "Callback url". Input something as "Secret", our code doesn't care much about it. Tick "message_deliveries", "messages", "messaging_optins" and "messaging_postbacks". Click "Verify and Save". You will be back to previous page. In "webhooks" section, select page and click "subscribe".


pip install Flask

pip install requests


Run server :  python server.py



The code here accepts a message, retrieves the user id and the message content. It reverses the message and sends back to the user. For this we use the ACCESS_TOKEN we generated before hand. The incoming request must be responded with a status code 200 to acknowledge the message. Otherwise Facebook will try the message a few more times and then disable the webhook. So sending a http status code 200 is important. We just output “ok” to do so.
