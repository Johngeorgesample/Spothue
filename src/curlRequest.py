import requests
import json
from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


headers = {
	'Authorization': 'Bearer BQCcNFDzNV0SMo5JDRgNzpDDqCAseeyS0yMmG4mGhWjW0n6HUoRzp0sgfgMI7sgBxs1cgJUyy84V7bSon8cC7l_MiMgPYIRQF-YY2gFtkXurSsRwvoQnt0kFVK4eCjlk1WH-Cp27tNCd3_vgmA',
}

f = open("songIdLog.txt", "r")
spotify,track,mySong=str.split(f.read().strip()	, ':')
f.close()

response = requests.get("https://api.spotify.com/v1/tracks/" + str(mySong), headers=headers)

# print(response.text)

@app.route('/')
def index():
	return response.text