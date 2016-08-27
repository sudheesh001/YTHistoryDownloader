# The MIT License (MIT)
# 
# Copyright (c) 2016 Sudheesh Singanamalla
# Permission is hereby granted, free of charge, to any person 
# obtaining a copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the
# Software, and to permit persons to whom the Software is furnished to do so, subject 
# to the following conditions:
# The above copyright notice and this permission notice shall be included in all 
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
# FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


import os
import subprocess
# Subprocess is required because it executes the youtube-dl binary

lines = [line.rstrip('\n') for line in open('chrome_history.csv')]
# Reads all the lines from the CSV file generated from chrome_to_csv.py

for line in lines:
	givenLineArr = line.split(',')
	link = givenLineArr[0]
	print 'Downloading : ' + givenLineArr[1]
	if "youtube.com/watch" in link:
		download_link = link
		# Download the video and audio
		queryConstruction = 'youtube-dl ' + download_link
		# To Download only the audio
		# [LATER]: Use an argparse flag to download
		# queryConstruction = 'youtube-dl --extract-audio --audio-format mp3 ' + download_link 
		subprocess.call(queryConstruction, shell=True)

