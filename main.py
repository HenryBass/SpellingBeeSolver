import pyautogui
import time
from string import ascii_uppercase as blacklist

alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

letters = "hanycpo"

letters_list = ["h", "a", "n", "y", "c", "p", "o"]

main_letter = "o"

blacklist += "-."

for x in letters_list:
  alphabet_list.remove(x)

blacklist += ("".join(alphabet_list))

f = open("words.txt", "r") 
i = 0

time.sleep(10)

while i < 1000000:
    line = f.readline()
    if main_letter in line and len(line) > 5 and any(x for x in blacklist if x in line) == False:
        print(line)
        pyautogui.typewrite(line)
        pyautogui.press("Enter")
    i+=1

print("done")

