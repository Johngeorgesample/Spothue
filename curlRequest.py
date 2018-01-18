import requests
import json

headers = {
	'Authorization': 'Bearer BQDK_np0oVsRnbJ74abgU3WTPw6vdMqfKnsJ7ZtX2sQu_CKtlGbGiZtOKapbpYTNDcvQQ96xqebJZH9y8YO8cAnxE1aEL0StxPuS5lO5NGtQlKdDm5Vos3uaTr_ljBwot4U9Pd0p_R23RY0SBr9ZSK0',
}

f = open("songIdLog.txt", "r")
spotify,track,mySong=str.split(f.read().strip()	, ':')
f.close()

response = requests.get("https://api.spotify.com/v1/tracks/" + str(mySong), headers=headers)

print(response.text)

payload = open("payload.txt","w")
payload.write(response.text)
payload.close()