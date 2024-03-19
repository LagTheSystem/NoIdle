import keyboard as kb
from time import sleep


enabled = false
print("NoIdle 1.3-rc1")
print("By LagTheSystem\n")
print("To stop macro, close this window!")
sleep(1)
def enable():
    kb.remove_hotkey('f10')
    kb.add_hotkey('f10', disable)
    enabled = true
def disable():
    enabled = false
    kb.remove_hotkey('f10')
    kb.add_hotkey('f10', enable)
kb.add_hotkey('f10', enable)
while true:
    kb.KEY_DOWN('W')
    sleep(0.5)
    kb.KEY_UP('W')
    sleep(0.5)

