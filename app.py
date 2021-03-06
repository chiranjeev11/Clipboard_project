import pyperclip as pc 
from pynput import keyboard
import tkinter as tk
import time




last_data = [None]

def paste_fun():

	time.sleep(0.1)
	
	data = pc.paste()

	print(data)

	if data != last_data[0]:

		last_data[0] = data

		try:

			with open('text_data.txt', 'a') as f:

				f.write(data)
				f.write('\n')
		except:

			f = open('text_data.txt', 'w')
			f.write(data)



# The key combination to check
COMBINATIONS = [
    {keyboard.Key.ctrl, keyboard.KeyCode(char='c')},		# Use cmd instead of ctrl, if using mac 
    {keyboard.Key.ctrl, keyboard.KeyCode(char='C')}
]

# The currently active modifiers
current = set()


def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            paste_fun()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

