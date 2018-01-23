import requests
import json
from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


headers = {
	'Authorization': 'Bearer BQAMvz2MWr_GmbDpj-cZ4sgQL4HAg8LxFuNNr0Dehugk_XnA1hJJnP3n0MS07xmGKDMhZ1Rz3XjIRJ89poBFNfuJRrwpCoJOQmCF8hcYGF-kgR9shTFz2ChAukQYDrVrysifsATJaJaDHjcdPQ',
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