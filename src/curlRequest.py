import requests
import json
from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


headers = {
	'Authorization': 'Bearer BQA39Wj-Sa_H-GQ5yDp1HdQ4VqpnQdci87p22JRz08bpYxAPNxM5TvC2gNP2SNkP5VFzS9JIp5M272J5yQI9UgjuKcUt7bW0FxiF_XK7m-0_ZJvDmTwhRqbk8aIgCUUD1TpM83vbOKi3hi6HFA',
}

f = open("songIdLog.txt", "r")
spotify,track,mySong=str.split(f.read().strip()	, ':')
f.close()

response = requests.get("https://api.spotify.com/v1/tracks/" + str(mySong), headers=headers)

print(response.text)

payload = open("payload.txt","w")
payload.write(response.text)
payload.close()

@app.route('/')
def index():
	return response.text