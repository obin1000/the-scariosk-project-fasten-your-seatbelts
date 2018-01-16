from tkinter import *
import time

class gui:

	windows = Tk()
	windows.title('Scariosk')
	windows.geometry("800x400")
	windows.configure(background="black")
	windows.attributes('-fullscreen', True)
	windows.bind("q", quit)

	corendon = PhotoImage(file = 'scariosk.gif')
	test = PhotoImage(file = 'test.gif')
	testok = Label(windows, image=corendon)
	testok.place(x=0,y=0)
	tello = Label(windows, image=test)

	def quit(self):
		windows.destroy()


	def change(self):
		testok.place_forget()
		tello.place(x=0,y=0)

	windows.bind("1", change)

##windows.mainloop()