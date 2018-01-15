##Maak alvast triggerButton methodes, 3x if condities gebruiken: van dia 1 naar dia2, van dia2 naar dia3, van dia3 naar dia 4
##Bij dia 3 gaat camera aan, wordt aangetoond met camera.start_preview() en camera.stop_preview(). We gebruiken ook time.sleep(werkt wel hier aangezien t een input is)

from tkinter import *
import time

windows = Tk()
windows.title('Scariosk')
windows.geometry("800x400")
windows.configure(background="black")
windows.attributes('-fullscreen', True)
windows.bind("q", quit)

def quit(self):
    windows.destroy()

frameBegin = Frame(windows)
canvas = Canvas(frameBegin,highlightthickness = 0, width = 800, height = 400)
canvas.pack
corendon = PhotoImage(file = 'scariosk.gif')
test = PhotoImage(file = 'test.gif')
##canvas.create_image(0, 0, image = corendon, anchor = NW)
frameBegin.grid()
test = Label(windows, image=corendon)
test.place(x=0,y=0)
test1 = Label(windows, image=test)

def change(self):
	test.place_forget()
	test1.place(x=0,y=0)

windows.bind("1", change)

windows.mainloop()
