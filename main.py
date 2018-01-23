from tkinter import *
import time
import pygame

#Imports zelf gemaakt
from camera import foto
from gpio import gpio
from database import database


def quit(self):
    windows.destroy()

def selectFrame(frame):
    frame.tkraise()

def codeLabel(code):
    codeLabel = Label(f3, highlightthickness=0, borderwidth=0, font=("Times",50), text=code)
    codeLabel.configure(background='black', foreground='darkred')
    codeLabel.place(anchor="c", relx=.5, rely=.5)
    
def task():
    if io.triggerButton():
            code = base.generateCode()
            
            cam.liveStart()
            time.sleep(5)
            cam.liveStop()
            
            pygame.mixer.music.play()
            io.motorLanseer()
            time.sleep(0.2)
            io.flitsAan()
            
            selectFrame(f2)
            windows.update()
            
            cam.takePictures(code,6)
            time.sleep(0.5)
            
            io.flitsUit()
            io.motorReset()
            time.sleep(0.2)
            io.motorPause()
            
            codeLabel(code)
            selectFrame(f3)
            windows.update()
            
            base.insertData(code,(path + str(code)))
            
            time.sleep(20)
            selectFrame(f1)
            windows.update()
    windows.after(100, task)
    
path = '/home/pi/Fotos/'
base = database()
io = gpio()
cam = foto()

pygame.mixer.init()
pygame.mixer.music.load("media/scream.mp3")

cam.savePath(path)
cam.saveResolutie(1920,1080)
cam.saveRotation(False,False)
cam.saveFramerate(10)
cam.setupCamera()

io.motorPause()
io.flitsUit()


windows = Tk()
windows.title('Scariosk')
windows.geometry("800x480")
windows.configure(background="black")
windows.attributes('-fullscreen', True)
windows.config(cursor='none')


f1 = Frame(windows)
f2 = Frame(windows)
f3 = Frame(windows)

for frame in (f1, f2, f3):
    frame.grid(row=0, column=0, sticky='news')
    
startImage = PhotoImage(file = 'media/intro.gif')
scareImage = PhotoImage(file = 'media/eng.gif')
codeImage = PhotoImage(file = 'media/code.gif')

Label(f1, highlightthickness=0, borderwidth=0, image=startImage).pack()
Label(f2, highlightthickness=0, borderwidth=0, image=scareImage).pack()
Label(f3, highlightthickness=0, borderwidth=0, image=codeImage).pack()

windows.bind("q", quit)

selectFrame(f1)

windows.after(100, task)
windows.mainloop()