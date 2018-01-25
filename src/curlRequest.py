import requests
import json
from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


headers = {
	'Authorization': 'Bearer BQDAkrTdBEzc-uZnqgTSa72u8VehLq94cluRLi_jbe0s_i3259RwWsZR89_HCTOj8yDsW58mAvewDy0fD88GQhvF0_t1wW-nwp470qKhw25IcK6cX6GSQtismAEhfKOwqTiMiw4oenLHuJBHvA',
}

f = open("songIdLog.txt", "r")
spotify,track,mySong=str.split(f.read().strip()	, ':')
f.close()

response = requests.get("https://api.spotify.com/v1/tracks/" + str(mySong), headers=headers)

# print(response.text)

@app.route('/')
def index():
	return response.text