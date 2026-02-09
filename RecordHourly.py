import os
import time
import datetime
h = datetime.timedelta(hours=1)
while True:
    for i in range(1, 12):
        dt1 = datetime.datetime.fromtimestamp(time.time())
        dt2 = dt1.replace(minute=0, second=0)
        folder = f"{dt1.year}/{dt1.month}/{dt1.day}/{dt1.hour}/{i}"
        os.makedirs(folder)
        os.popen(f"ffmpeg -t {h - (dt1 - dt2)} -i 'rtsp://admin:@192.168.1.108:554/trackID={i}' -y -c copy '{folder}/{dt1.minute}.{dt1.second}.mp4' -c copy -f matroska pipe:1 | ffplay -autoexit -i -")
        time.sleep(0.5)
    dt1 = datetime.datetime.fromtimestamp(time.time())
    dt2 = dt1.replace(minute=0, second=0)
    time.sleep((h - (dt1 - dt2)).seconds)
