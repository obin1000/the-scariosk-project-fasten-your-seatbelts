#Imports geleend van anderen
import time
import pygame

#Imports zelf gemaakt
from camera import foto
from gpio import gpio
from database import database
from randomCode import randomCode
from gui import gui

if __name__ == "__main__":
    
    path = '/home/pi/Fotos/'
    base = database()
    io = gpio()
    cam = foto()
    ui =gui()
    
    ui.windows.mainloop()
    
    pygame.mixer.init()
    pygame.mixer.music.load("media/part1.mp3")
    
    cam.savePath(path)
    cam.saveResolutie(1920,1080)
    cam.saveRotation(False,False)
    cam.saveFramerate(10)
    cam.setupCamera()

    io.motorPause()
    io.flitsUit()
    
    while True:
        time.sleep(2)
        if io.triggerButton():
            code = randomCode().generateCode()
            io.flitsAan()
            io.motorLanseer()
            time.sleep(0.5)
            pygame.mixer.music.play()
            cam.takePictures(code,6)
            io.flitsUit()
            io.motorReset()
            time.sleep(1)
            io.motorPause()
            base.insertData(code,(path + str(code) + '.jpg'))
            time.sleep(2)