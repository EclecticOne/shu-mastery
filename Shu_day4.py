import time
import winsound
import os
from datetime import datetime

def clear():
    os.system('cls')


frames =[
    "    *    \n  *   *  \n*       *\n  *   *  \n    *    ",
    "  *   *  \n*       *\n    *    \n*       *\n  *   *  ",
    "    *    \n  *   *  \n*       *\n  *   *  \n    *    ",
    "  *   *  \n*       *\n    *    \n*       *\n  *   *  "
]

print("SHU Day 4: SPINNING MERKABA\n")

for i in range(3):
    clear()
    print(f"BREATH {i+1}: IN 8... HOLD 4... OUT 8...\n")
    print(frames[i % 4])
    time.sleep(24)
    winsound.Beep(1000,500)

log_entry = f"Day 4 | {datetime.now().strftime('%Y-%m-%d %H:%M')} | Sensation: ____ | Word: ____\n"
with open("merkaba_log.txt", "a") as f:
    f.write(log_entry)

print("\nSPIN COMPLETE. edit merkaba_log.txt with your sensation.")