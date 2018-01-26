import requests
import json
from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


headers = {
	'Authorization': 'Bearer BQA_6Fyh9OJ6XIN6qQ4hA3p3Afo_8RWzoVWmsdjvaNGPuQG1TJQJFNnbVt8NdF2p2JBuBTBMqcAAnRHiSxPSWa58AQtNN21y6bNLIxDYwtKs0y_E3W27_3FWW_lAz5pCXxbisnZf2V_DKHT_ZQ',
}

f = open("songIdLog.txt", "r")
spotify,track,mySong=str.split(f.read().strip()	, ':')
f.close()

response = requests.get("https://api.spotify.com/v1/tracks/" + str(mySong), headers=headers)

# print(response.text)

@app.route('/')
def index():
	return response.text