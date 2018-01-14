from tkinter import *
import time

windows = Tk()
windows.title('Scariosk')
windows.geometry("800x400")
windows.configure(background="white")
windows.attributes('-fullscreen', True)
windows.bind("q", quit)

def quit(self):
    windows.destroy()
    
frame3 = Frame(windows)
frame3.grid()
frame3.isgridded = True
drie = Canvas(frame3, highlightthickness = 0, width = 800, height = 400)
drie.pack()
drie.configure(background = "white")
drie.create_text(350, 125, anchor = N, font = "Helvetica 70", fill = "darkred", text = "3....")

frame2 = Frame(windows)
frame2.isgridded = False
twee = Canvas(frame2, highlightthickness = 0, width = 800, height = 400)
twee.pack()
twee.configure(background="white")
twee.create_text(350, 125, anchor = N, font = "Helvetica 70", fill = "darkred", text = "2....")

frame1 = Frame(windows)
frame1.isgridded = False
een = Canvas(frame1, highlightthickness = 0, width = 800, height = 400)
een.pack()
een.configure(background="white")
een.create_text(350, 125, anchor = N, font = "Helvetica 70", fill = "darkred", text = "1....")

frameGo = Frame(windows)
frameGo.isgridded = False
een = Canvas(frameGo, highlightthickness = 0, width = 800, height = 400)
een.pack()
een.configure(background="white")
een.create_text(350, 125, anchor = N, font = "Helvetica 70", fill = "darkred", text = "Smile!!")

def switchThreeToTwo(self):
	if (frame3.isgridded):
		frame3.grid_forget()
		frame3.isgridded = False
		frame2.isgridded = True
		frame2.grid()

windows.bind("3", loop)


windows.mainloop()