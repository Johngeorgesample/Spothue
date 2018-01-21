import requests
import json
from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


headers = {
	'Authorization': 'Bearer BQB_TASql8DQvfQjSGlvjXFrSJB18mhq2DPbng3Chllwd6WhPiGygyvp37BkzUbB1yJmB2I8Y9zLaFIxoapOQFvJSQuJUDOHswEq2oVFmU6ZSjkNDnz0y5DXQlbj-r_7AmmkjHMfgjA7uTrsSF_7-gY',
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