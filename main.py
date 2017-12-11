#Imports geleend van andere mensen
import time
#from threading import Thread

#Imports zelf gemaakt
from camera import foto
from gpio import gpio
from database import database
from randomCode import randomCode

if __name__ == "__main__":
    
    path = '/home/pi/Documents/'
    base = database()
    iobord = gpio()
    maakFoto = foto()
    
    maakFoto.savePath(path)
    maakFoto.saveResolutie(1920,1080)
    maakFoto.saveRotation(False,False)
    maakFoto.setupCamera()
    
    while True:
        if iobord.triggerButton():
            code = randomCode().generateCode()
            maakFoto.takePictures(code,6)
            base.insertData(code,(path + str(code)))
        time.sleep(1)
    #Thread(target = ).start()