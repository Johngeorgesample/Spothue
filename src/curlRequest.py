import requests
import json
from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


headers = {
	'Authorization': 'Bearer BQCiRWpn2YSV6Kw54F3nw8aFc3hN99TAIgnwx-XEaLa9V33R9Awn_ohOMvNdmGpHC4t8mtzjY26Ytif1w9LhDfyl6CHm9Jfa1BAY0wKuZJ2P7JFCP-eOUmG1JjnggDoQlOZUcniHIhh2IOFsPA',
}

f = open("songIdLog.txt", "r")
spotify,track,mySong=str.split(f.read().strip()	, ':')
f.close()

response = requests.get("https://api.spotify.com/v1/tracks/" + str(mySong), headers=headers)

# print(response.text)

@app.route('/')
def index():
	return response.text