import requests
import json
from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


headers = {
	'Authorization': 'Bearer BQBmoKZHhE0vPV0J2te_vK7co1wJrAg-6p-XC2jSM02fVfmaG8xbE4aJDTmNhQ477HzPrv3WIqMOtovGjJsvtPO6xQLr8k_QwvknumxmJkBv3wwkSyWaOKp-SO3g1Z0guADO3xRaAzXBJSz0Vg',
}

f = open("songIdLog.txt", "r")
spotify,track,mySong=str.split(f.read().strip()	, ':')
f.close()

response = requests.get("https://api.spotify.com/v1/tracks/" + str(mySong), headers=headers)

# print(response.text)

@app.route('/')
def index():
	return response.text