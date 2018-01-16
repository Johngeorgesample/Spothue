#!/usr/bin/env python
import os

writeFileCmd = """osascript -e 'set albumID to "ALBUM ID HERE" 
				 set textFile to "/Users/johngeorgesample/Desktop/albumIdLog.txt"

				 do shell script "echo  " & quoted form of albumID & " >  " & quoted form of textFile'"""


def createIdLog():
     os.system(writeFileCmd)
createIdLog()