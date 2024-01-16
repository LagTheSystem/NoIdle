import keyboard
from time import sleep

count = 0
print("NoIdle 1.1.0")
print(" ")
print("---Changelog---")
print(" - Removed mouse module to make loading faster and have higher compatibility")
print(" ")
print("By herobrick360")
print("To stop macro x out this window!")
while count == 0:
    sleep(1)
    keyboard.press_and_release('w')

