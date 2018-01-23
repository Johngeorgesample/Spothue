#!/bin/bash
osascript createLog.applescript
export FLASK_APP=curlRequest.py
flask run

