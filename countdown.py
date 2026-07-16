import time

val = int(input("Enter time in seconds: "))

for i in range (val,0,-1):
    second = i%60
    minute = int(i/60) % 60
    hour = int(i/3600)
    print(f"{hour:02}:{minute:02}:{second:02}")
    time.sleep(1)
print("Time's up!")