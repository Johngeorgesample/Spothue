# Spothue

Application that matches Philips Hue lights to the most dominant colors of Spotify's current song album art.

## What It Does
In its current state, Spothue can:
* save current song's id to text file
* receive Spotify API payload
* write payload to local webserver using [Flask](http://flask.pocoo.org/)

## Usage
1. Change textFile path in `createLog.applescript` to your preferred location
2. Compile `createLog.applescript`
3. Generate temporary bearer token [from Spotify's API console](https://developer.spotify.com/web-api/console/get-track/) and add it to headers in `curlRequest.py`
4. Execute `curlRequest.py`

## Todo

