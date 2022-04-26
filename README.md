it converts all videos in a given directory and removes website names from file names so that plex/jellyfin/emby can recognize and show perfect metadata for the given videos.

It won't convert the same file again , it checks if it is already converted and skips if it has already converted.so my recommendation is to run this python file using "screen" and also use "crontab" to schedule it to run daily, so that it converts files when ever you add a new video in to that directory.
"""00 00 * * * screen -dmS jellyfin_convert ipython3 jellyfin_convert.py"""
it converts video in such a way that it is efficient in HTTP streaming and better suited for amazon firestick , it also suits for almost all devices .if you want to explicitly change the device , then you can give your device name . you can search your device name using '''HandBrakeCLI --preset-list'''.
