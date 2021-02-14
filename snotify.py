from time import sleep
from win10toast import ToastNotifier
from SwSpotify import spotify
toaster = ToastNotifier()
print("Welcome to Snotify!")
title = "Paused"
artist = "Paused"
while True:
	sleep(0.05)
	try:
		sp = spotify.current()
	except:
		continue
	else:
		if sp[0] != title:
			try:
				sp = spotify.current()
			except:
				continue
			else:
				title, artist = spotify.current()
				toaster.show_toast("",f"{artist} - {title}", duration=3, icon_path='snotify.ico')
	sleep(0.05)
