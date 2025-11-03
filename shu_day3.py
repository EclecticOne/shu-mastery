import time
import winsound

print("SHU DAY 3: Sound + Auto-Log")

for i in range(3):
    print(f"Breath {i+1}: IN 8... HOLD 4... OUT 8...")
    time.sleep(24)
    winsound.Beep(1000, 500)


with open("merkaba_log.txt", "a") as f:
    f.write("Day 3 | Sensation: ____ | Word: ____\n")

print("LOG SAVED. Check merkaba_log.txt")