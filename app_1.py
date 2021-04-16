import tkinter as tk 
import pyperclip as pc 

window = tk.Tk()

window.title('Clipboard')

window.geometry("1350x750+0+0")

def refresh():

	try:
		with open('text_data.txt', 'r') as f:

			data_list = []

			for line in f:

				data_list.append(line)
	except:

		f = open('text_data.txt', 'w') 
		data_list=[]


	return data_list


def copy_text(text):

	pc.copy(text)
	print('hello')


def display(window1):


	window1.withdraw()

	window = tk.Toplevel(window1)

	window.geometry("1350x750+0+0")

	label = tk.Label(window, text='Clipboard Logs', width = 30, font = ( "arial", 52, "bold" )).grid()

	tk.Button(window, text='Refresh', command=lambda: display(window)).grid()

	data_list = refresh()

	for index in range(len(data_list)):

		# # button = tk.Button(window, text='{}'.format(data_list[index]), command=lambda: copy_text(button.text)).grid()

		ent = tk.Entry(window, state='readonly', readonlybackground='white', fg='black')
		var = tk.StringVar()
		var.set(data_list[index])
		ent.config(textvariable=var, relief='flat')
		ent.grid()



label = tk.Label(window, text='Clipboard Logs', width = 30, font = ( "arial", 52, "bold" )).grid()

# tk.Button(window, text='Refresh', command=display(window)).grid()


display(window)








window.mainloop()