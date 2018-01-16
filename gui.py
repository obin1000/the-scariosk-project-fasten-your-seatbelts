from tkinter import *
import time


def quit(self):
    windows.destroy()

def selectFrame(frame):
    frame.tkraise()

def updateScherm():
    while True:
        windows.update_idletasks()
        windows.update()

windows = Tk()
windows.title('Scariosk')
windows.geometry("800x480")
windows.configure(background="black")
windows.attributes('-fullscreen', True)
windows.bind("q", quit)
windows.bind("1", selectFrame(f2))

f1 = Frame(windows)
f2 = Frame(windows)
f3 = Frame(windows)

for frame in (f1, f2, f3):
    frame.grid(row=0, column=0, sticky='news')
    
testImage = PhotoImage(file = 'media/test.gif')
buttonImage = PhotoImage(file = 'media/scariosk.gif')
Label(f1, image=buttonImage).pack()
Label(f2, image=testImage).pack()
selectFrame(f1)

windows.mainloop()

