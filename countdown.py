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

corendon = PhotoImage(file = 'scariosk.gif')
test = PhotoImage(file = 'test.gif')
##canvas.create_image(0, 0, image = corendon, anchor = NW)
test = Label(windows, image=corendon)
test.place(x=0,y=0)
test1 = Label(windows, image=test)
test2 = Label(windows, image=test1)
test3 =
test4 =

def change(self):
	test.place_forget()
	test1.place(x=0,y=0)
	
def change2(self):
	test1.place_forget()
	test2.place(x=0,y=0)
	
def change3(self):
	test2.place_forget()
	test3.place(x=0,y=0)

def change4(self):
    test3.place_forget()
    test4.place(x=0,y=0)
	
def repeat(self):
	test4.place_forget()
	test.place(x=0,y=0)

windows.bind("1", change)

windows.mainloop()
