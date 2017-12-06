#Imports geleend van andere mensen
import time

#Imports zelf gemaakt
from camera import foto
from gpio import gpio
#from database import database
#from randomCode import randomCode

if __name__ == "__main__":

    #code = randomCode()
    #print(code.generateCode())
    #base = database()
    knop = gpio()
    maakFoto = foto()
    #base.insertData('69','lol/lal')

    maakFoto.savePath('/home/pi/Documents/')
    maakFoto.saveResolutie(1920,1080)
    maakFoto.saveRotation(True, True)
    maakFoto.setupCamera()
    while True:
        if knop.triggerButton():
            maakFoto.takePictures(1345,6)
            time.sleep(1)  
    