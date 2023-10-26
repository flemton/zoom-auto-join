import schedule
import time
import webbrowser

zoom_link = "https://microverse.zoom.us/j/91369660757?pwd=MmRQZ2Ywa0NEb052ZlF5cXNka09Rdz09"

def join_meeting():
    print('Joining')
    webbrowser.get().open(zoom_link)
    print('Joined')

schedule.every().day.at("17:08").do(join_meeting)

while True:
    schedule.run_pending()
    time.sleep(1)
