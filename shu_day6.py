import time
import winsound
import os
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

def clear():
    os.system('cls')

frames = [
    "    *    \n  *   *  \n*       *\n  *   *  \n    *    ",
    "  *   *  \n*       *\n    *    \n*       *\n  *   *  ",
    "    *    \n  *   *  \n*       *\n  *   *  \n    *    ",
    "  *   *  \n*       *\n    *    \n*       *\n  *   *  "
]

def energy_bar(level):
    filled = '█' * level
    empty = '░' * (10 - level)
    if level < 7:
        color = Fore.GREEN

    elif level <10:
        color = Fore.YELLOW
    else:
        color = Fore.Red
    return f"{color}{filled}{empty}{Style.RESET_ALL}{level}/10"

print("SHU DAY 6: SPIN + ENERGY BAR\n")

energy = 0 
for i in range(3):
    clear()
    energy += 3
    print(f"BREATH {i+1}: IN 8... HOLD 4... OUT 8...\n")
    print(frames[i % 4])
    print(f"\nEnergy: {energy_bar(energy)}")
    time.sleep(24)
    winsound.Beep(1000, 500)

log_entry = f"Day 6 | {datetime.now().strftime('%Y-%m-%d %H:%M')} | Sensation: _____ | Word: ____ \\n"
with open("merkaba_log.txt", "a") as f:
    f.write(log_entry)

print("\nFIELD FULL. Edit merkaba_log.txt with yuour sensation.")