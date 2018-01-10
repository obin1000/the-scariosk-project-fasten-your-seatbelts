from tkinter import *
def quit(self):
    windows.destroy()
    
windows = Tk()
windows.title('Scariosk')
windows.geometry("800x400")
windows.configure(background="white")
windows.attributes('-fullscreen', True)
windows.bind("q", quit)
    
def countDown3(self):
    drie = Canvas(windows, highlightthickness = 0, width = 800, height = 400)
    drie.pack()
    drie.configure(background="white")
    drie.create_text(400, 200, achter = N, font = "Helvetica 40", fill = "darkred", text = "3....")
    
def countDown2(self):
    twee = Canvas(windows, highlightthickness = 0, width = 800, height = 400)
    twee.pack()
    twee.configure(background="white")
    twee.create_text(400, 200, achter = N, font = "Helvetica 40", fill = "darkred", text = "2....")
def countDown1(self):
    een = Canvas(windows, highlightthickness = 0, width = 800, height = 400)
    een.pack()
    een.configure(background="white")
    een.create_text(400, 200, achter = N, font = "Helvetica 40", fill = "darkred", text = "1.... en nu komt het....")

def beginDia(self):
    tekst = Canvas(windows,highlightthickness = 0, width = 800, height = 30)
    canvas = Canvas(windows,highlightthickness = 0, width = 800, height = 200)
    canvas2 = Canvas(windows,highlightthickness = 0, width = 800, height = 200)
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