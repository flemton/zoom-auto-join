import schedule
import time
import webbrowser
import json
import os
from datetime import datetime

CONFIG_FILE = 'meetings.json'

def load_meetings():
    """Load meetings from config file"""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return []

def save_meetings(meetings):
    """Save meetings to config file"""
    with open(CONFIG_FILE, 'w') as f:
        json.dump(meetings, f, indent=2)

def join_meeting(meeting_name, zoom_link):
    """Open Zoom meeting in browser"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f'[{timestamp}] Joining meeting: {meeting_name}')
    try:
        webbrowser.get().open(zoom_link)
        print(f'[{timestamp}] Successfully opened {zoom_link}')
    except Exception as e:
        print(f'[{timestamp}] Error opening meeting: {e}')

def add_meeting(name, link, time_str, days=None):
    """Add a new scheduled meeting"""
    meetings = load_meetings()
    meeting = {
        'name': name,
        'link': link,
        'time': time_str,
        'days': days or ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
    }
    meetings.append(meeting)
    save_meetings(meetings)
    print(f"Added meeting '{name}' at {time_str}")

def schedule_meetings():
    """Schedule all meetings from config"""
    meetings = load_meetings()
    
    for meeting in meetings:
        days = meeting.get('days', ['monday'])
        for day in days:
            if day.lower() == 'monday':
                schedule.every().monday.at(meeting['time']).do(
                    join_meeting, meeting['name'], meeting['link']
                )
            elif day.lower() == 'tuesday':
                schedule.every().tuesday.at(meeting['time']).do(
                    join_meeting, meeting['name'], meeting['link']
                )
            elif day.lower() == 'wednesday':
                schedule.every().wednesday.at(meeting['time']).do(
                    join_meeting, meeting['name'], meeting['link']
                )
            elif day.lower() == 'thursday':
                schedule.every().thursday.at(meeting['time']).do(
                    join_meeting, meeting['name'], meeting['link']
                )
            elif day.lower() == 'friday':
                schedule.every().friday.at(meeting['time']).do(
                    join_meeting, meeting['name'], meeting['link']
                )
            print(f"Scheduled '{meeting['name']}' every {day} at {meeting['time']}")

def main():
    """Main entry point"""
    print("=" * 50)
    print("Zoom Auto Join")
    print("=" * 50)
    print("\nConfigured meetings:")
    print("-" * 50)
    
    schedule_meetings()
    
    print("-" * 50)
    print("Running... (Press Ctrl+C to stop)")
    print("=" * 50)
    
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\nStopping Zoom Auto Join...")
        print("Goodbye!")

if __name__ == "__main__":
    main()
