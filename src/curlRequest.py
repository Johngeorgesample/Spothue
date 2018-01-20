import requests
import json
from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


headers = {
	'Authorization': 'Bearer BQCCCP-FEoYTcs36pM8vsbyypBQ_8TWF-7LtgIxqpg914CxCBEbnX30ZbA5Jq0NcMzhlHtgOs85whBaABmDUaAaxSiP4GNkIcMcSm9fOg_HaBETjXVtNGmqTcrXw1ZKn45vmIS0tv45DjhbI7deZyk4',
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