import schedule
import time
import webbrowser

def zoom_link(meeting_link):
    webbrowser.open(meeting_link)

def join_meeting():
    print('Joining')
    zoom_link('google.com')
    print('Joined')

schedule.every().day.at("06:13").do(join_meeting)

while True:
    schedule.run_pending()
    time.sleep(1)
