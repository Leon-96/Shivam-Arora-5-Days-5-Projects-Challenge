import time
import webbrowser

def youtube_player():
    link = "https://www.youtube.com/watch?v=xJK3FrOHoxg"
    webbrowser.open_new(link)

    time.sleep(3600)

youtube_player()


#  to run this script in background in linux you can use crontab to run it as a daemon in background so  add this line 
# 0 * * * * /path of Day1-youtube_player.py to run the code in the background 
