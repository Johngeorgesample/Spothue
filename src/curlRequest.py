import requests
import json
from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


headers = {
	'Authorization': 'Bearer BQDw3tWKUI-eIRPnRYO9hQ4zFmLq0BZVutYiTlI0DbTQzsfSOUo2tliqkIDKt4ThyJkDVNiMb0SwlgTUFa7-HEuJB820KdhsycdzJoAdM22KCxrU01-Zae1CEUoHUbDPlpOsYS9YfOi5hDxSFg',
}

f = open("songIdLog.txt", "r")
spotify,track,mySong=str.split(f.read().strip()	, ':')
f.close()

response = requests.get("https://api.spotify.com/v1/tracks/" + str(mySong), headers=headers)

# print(response.text)

payload = open("payload.txt","w")
payload.write(response.text)
payload.close()

@app.route('/')
def index():
	return response.text