# Snotify

A Python-driven utility to notify Windows 10 users when Spotify song changes

Usage: Just run the file (either python snotify.py or the compiled exe) and it will notify you when Spotify title changes.

##Installing requirements
pip install -r requirements.txt
or
pip3 install -r requirements.txt
## Compiling

You will need cx_freeze on a Windows 10 machine and the following libraries:

win10toast - for notifications

SwSpotify - for the title acquiring of Spotify

Compiling can be done by running:
python setup.py build 
