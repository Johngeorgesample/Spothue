import requests

headers = {
	'Authorization': 'Bearer BQCoyqhhoM1EwMfJwfsU7h5fVWnJjA4seaiHFRriLveqIL_V2Rl2Ym68oLyuWIv6Z0FugqmuNyvRCT_WWtByEvjZYH5MSkg12t8_7VE-3HCPuXJpPq5btqOqjbAoyQ0kLXdTon-EvSrQPLHuV9kNdOY',
}

response = requests.get('https://api.spotify.com/v1/tracks/' + '0pVaTi1RHV9lUZJ12ciS7P', headers=headers)

print(response.json())

