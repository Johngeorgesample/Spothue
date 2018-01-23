import requests
import json
from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


headers = {
	'Authorization': 'Bearer BQCR8fHhXW3I5lpPUxdKzAKA5Uzw_yjtOr1X442RlmwE4Wc4fs7hUdBG9XOfGHG7Tl-rTeEFTgOlFFsUB9fg4Lj8nUZruU3B5P8wCdBulvOOOCU8fr8lSCvupf_ux1jroHeMwmWA58hbsy7rUA',
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