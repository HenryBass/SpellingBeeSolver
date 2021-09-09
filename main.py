import pyautogui
import time
from string import ascii_uppercase as blacklist

alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

letters = input("Ring Letters (Format x x x x x x): ")

letters_list = letters.split(" ")
print(letters_list)

main_letter = input("Core Letter: ")

blacklist += "-."

for x in letters_list:
  try:
    alphabet_list.remove(x)
    print(alphabet_list)
  except:
    print("Letters Entered Incorrectly")

blacklist += ("".join(alphabet_list))

f = open("words.txt", "r") 
i = 0

size = sum(1 for _ in f)

while i < size:
    line = f.readline()
    if main_letter in line and len(line) > 5 and any(x for x in blacklist if x in line) == False:
        print(line)
        pyautogui.typewrite(line)
        pyautogui.press("Enter")
    i+=1

print("done")

