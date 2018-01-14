from tkinter import *
def quit(self):
    windows.destroy()
    
windows = Tk()
windows.title('Scariosk')
windows.geometry("800x400")
windows.configure(background="white")
windows.attributes('-fullscreen', True)
windows.bind("q", quit)
    
def countdown3(self):
    frame3 = Frame(windows)
    frame3.grid()
    drie = Canvas(frame3, highlightthickness = 0, width = 800, height = 400)
    drie.pack()
    drie.configure(background = "white")
    drie.create_text(700, 125, anchor = N, font = "Helvetica 70", fill = "darkred", text = "3....")
    
def countdown2(self):
    frame2 = Frame(windows)
    frame2.grid()
    twee = Canvas(frame2, highlightthickness = 0, width = 800, height = 400)
    twee.pack()
    twee.configure(background="white")
    twee.create_text(350, 125, achter = N, font = "Helvetica 70", fill = "darkred", text = "2....")
    
def countdown1(self):
    frame1 = Frame(windows)
    frame1.grid()
    een = Canvas(frame1, highlightthickness = 0, width = 800, height = 400)
    een.pack()
    een.configure(background="white")
    een.create_text(350, 125, achter = N, font = "Helvetica 70", fill = "darkred", text = "1....")
    
def countdownGo(self):
    frameGo = Frame(windows)
    frameGp.grid()
    een = Canvas(frameGo, highlightthickness = 0, width = 800, height = 400)
    een.pack()
    een.configure(background="white")
    een.create_text(350, 125, achter = N, font = "Helvetica 70", fill = "darkred", text = "Smile!!")

def beginDia(self):
    frameBegin = Frame(windows)
    frameBegin.grid()
    tekst = Canvas(frameBegin,highlightthickness = 0, width = 800, height = 30)
    canvas = Canvas(frameBegin,highlightthickness = 0, width = 800, height = 200)
    canvas2 = Canvas(frameBegin,highlightthickness = 0, width = 800, height = 200)
    canvas.pack()
    tekst.pack()
    canvas2.pack()
    canvas.configure(background="white")
    tekst.configure(background = "white")
    canvas2.configure(background="white")
    corendon = PhotoImage(file = 'don.gif')
    arrow = PhotoImage(file = 'arrow.gif')
    corendon = corendon.subsample(3,3)
    arrow = arrow.subsample(3,3)
    tekst.create_text(400, 0, anchor = N, font = "Helvetica 20", fill = "darkred", text = "Druk op de knop")
    canvas2.create_image(400,-80,anchor = N, image = arrow)
    canvas.create_image(400,0,anchor = N, image = corendon)


windows.mainloop()