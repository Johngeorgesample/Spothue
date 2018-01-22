import requests
import json
from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


headers = {
	'Authorization': 'Bearer BQA_6Zainw7AMR8OTGlODlAlYiNvLTdz7MyPfUU507PuEtxYB3wDHveJ7GGe_qkBOGT7_GG9om7dc_U0NmF_bXN3Wgoax7Mv5gSp1mX5fihJ58O9_p1u0Nuc4frU9EM9sOJ0FrkkIqwK2HdEd0645es',
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