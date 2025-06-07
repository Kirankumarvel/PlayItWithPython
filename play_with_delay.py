from playsound import playsound
import time

# Play sound 3 times with a 2-second pause between
for i in range(3):
    playsound('notification.mp3')
    time.sleep(2)
