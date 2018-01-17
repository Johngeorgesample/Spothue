import requests

headers = {
	'Authorization': 'Bearer BQCu5U6vGrVSkOwHAwtnSd0f89JGdf-PIeT_obKB7SspgaBOcvukGi08qTxR5O2dENt3yvsa92uOKrfbTaAHB36bfkk4OzaCaz2-DwXGcye9X1Pu4Qd1wf1iubHwCPJrJmw0H5Yw7U3g4-LTmiJc07Q',
}

f = open("songIdLog.txt", "r")
spotify,track,mySong=str.split(f.read().strip()	, ':')
f.close()

response = requests.get("https://api.spotify.com/v1/tracks/" + str(mySong), headers=headers)

print(response.text)

