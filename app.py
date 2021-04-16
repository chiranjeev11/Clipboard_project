import pyperclip as pc 
from pynput import keyboard
import tkinter as tk




last_data = [None]

def paste_fun():

	data = pc.paste()

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
    {keyboard.Key.cmd, keyboard.KeyCode(char='c')},
    {keyboard.Key.cmd, keyboard.KeyCode(char='C')}
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

