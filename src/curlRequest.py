import requests
import json
from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


headers = {
	'Authorization': 'Bearer BQDe6mbNgXH6PxRBdDQaeWQwiizoz6fzpPgMyRMBOmQ5pmL8XFKwXGBvWrb7fsvE8gfFukppiio-450QSolrvq388y1moUvX-RYrgTN6yyN8Aw6EPtJ5HLFm6KE8WQXUjmUYsHcRw4UeuzFevg',
}

f = open("songIdLog.txt", "r")
spotify,track,mySong=str.split(f.read().strip()	, ':')
f.close()

response = requests.get("https://api.spotify.com/v1/tracks/" + str(mySong), headers=headers)

# print(response.text)

@app.route('/')
def index():
	return response.text