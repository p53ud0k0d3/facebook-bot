from flask import Flask, request
import requests

app = Flask(__name__)

ACCESS_TOKEN = " "

def reply(user_id, msg):
	data = {
		"recipient" : {"id": user_id},
		"message": {"text": msg}
	}
	resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
	print(resp.content)

@app.route('/', methods=['POST'])
def handle_incoming_message():
	data = request.json
	sender = data['entry'][0]['messaging'][0]['sender']['id']
	message = "si"
	reply(sender, message)
	return "ok"

if __name__ == '__main__':
	app.run(debug=True)
