import requests
import json
from flask import Flask
app = Flask(__name__)

headers = {
	'Authorization': 'Bearer BQCexT97lzpAaF_AQCkRKeayaBbU1sQ2M8SjbURjXIbexI05mebma4JLbTtIULrh2OnqeLdEicVJSPE5iCovGG_1V1vpA6_JFQtdEq13HwyKRFacPAzXdrhrqZbHZQr_iqJVAnGm6OpBTr1g0Bz_nXo',
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