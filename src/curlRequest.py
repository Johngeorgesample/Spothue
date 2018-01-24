import requests
import json
from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


headers = {
	'Authorization': 'Bearer BQBrkJ1RQPEzi873oFqD70D6fTUSUhm6alFB6PjvYO_YOSLH_lqd4UkQwWUIvQBOEhDWiOzDWzPo37ZzANr-m43osyXf6UtIipVnNouETcf-nyVuuQroom650BJENC1KMKJAlZg_ixp-WqztqA',
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