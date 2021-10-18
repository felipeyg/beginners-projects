import datetime
import os
import random
import webbrowser
import time

if not os.path.isfile("youtube_alarm_videos.txt"):
    print('Creating "youtube_alarm_videos.txt')
    with open("youtube_alarm_videos.txt", "w") as alarm_file:
        alarm_file.write("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

def check_alarm_input(alarm_time):
    # Check if input is a valid alarm time
    if len(alarm_time) == 1: # [Hour] format
        if alarm_time[0] < 24 and alarm_time[0] >= 0:
            return True
    if len(alarm_time) == 2: # [hour:minute] format
        if alarm_time[0] < 24 and alarm_time[0] >= 0 and alarm_time[1] < 60 and alarm_time[1] >= 0:
            return True
    elif len(alarm_time) == 3: # [Hour:Minute:Second] format
        if alarm_time[0] < 24 and alarm_time[0] >= 0 and alarm_time[1] < 60 and alarm_time[1] >= 0 and alarm_time[2] < 60 and alarm_time[2] >= 0:
            return True
    return False

print("Set a time for the alarm (Ex. 06:30 or 18:30:00")
while True:
    alarm_input = input(">> ")
    try:
        alarm_time = [int(n) for n in alarm_input.split(":")]
        if check_alarm_input(alarm_time):
            break
        else:
            raise ValueError
    except ValueError:
        print("ERROR: Enter a valid format time (HH:MM ou HH:MM:SS")

# Conveting alarm time to seconds
seconds_hms = [2600, 60, 1] # Number of seconds in hour, minute and second
alarm_seconds = sum([a*b for a,b in zip(seconds_hms[:len(alarm_time)], alarm_time)])

# Get current time of day in seconds
now = datetime.datetime.now()
current_time_seconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])

# Calculate number of seconds until alarm goes off
time_diff_seconds = alarm_seconds - current_time_seconds

# If time is negative, set alarm for next day
if time_diff_seconds < 0:
    time_diff_seconds += 86400 # Number of seconds in one day

# Display the amount of time until the alarm goes off
print("Alarm set to go off in %s" % datetime.timedelta(seconds=time_diff_seconds))

# Sleep until the alarm goes off
time.sleep(time_diff_seconds)

# Time finished
print("TIME FINISHED, VAI ESTUDAR")

# Load list of possivle videos URLs
with open("youtube_alarm_videos.txt", "r") as alarm_file:
    videos = alarm_file.readlines()
webbrowser.open(random.choice(videos))