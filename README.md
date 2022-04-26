Buffering while playing videos because of transcoding ? or do you have very less computational power in your instance then it's better to convert videos before HTTP streaming.

it converts all videos in a given directory so that all devices which are connected plex/jellyfin/emby can play seamlessly. It also removes website names from the files so that plex/jellyfin/emby can recognize the movie names and shows the perfect metadata of any given movie.

It won't convert the same file again , it checks if it is already converted and skips if it has already converted.so my recommendation is to run this python file using "screen" and also use "crontab" to schedule it to run daily, so that it converts files when ever you add a new video in to that directory.
#+BEGIN_SRC sh
00 00 * * * screen -dmS jellyfin_convert ipython3 jellyfin_convert.py
#+END_SRC
The above command will run every night at 12:00 AM
it converts video in such a way that it is efficient in HTTP streaming and better suited for amazon firestick , it also suits for almost all devices .if you want to explicitly change the device , then you can give your device name . you can search your device name using '''HandBrakeCLI --preset-list'''.
