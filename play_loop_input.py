from playsound import playsound

repeat = int(input("How many times should I play the sound? "))

for _ in range(repeat):
    playsound('alert.wav')
