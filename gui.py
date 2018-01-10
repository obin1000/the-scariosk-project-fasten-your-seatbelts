from tkinter import *
def quit(self):
    windows.destroy()
    
windows = Tk()
windows.title('Scariosk')
windows.geometry("800x400")
windows.configure(background="white")
windows.attributes('-fullscreen', True)
windows.bind("q", quit)
    
## countDown3(self):
## countDown2(self):
## countDown1(self):

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