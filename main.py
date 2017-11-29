#from camera import foto
#from button import button
from database import database

if __name__ == "__main__":
    base = database()
    if base.checkCode(69):
        print('code vrij')
    else:
        print('code niet vrij')
    #base.insertData('69','lol/lal')
    #knop = button()
    #maakFoto = foto()
    #maakFoto.saveResolutie(1920,1080)
    #maakFoto.savePath('/home/pi/Documents/')
    #while True:
    #    if knop.triggerButton():
    #        maakFoto.takePictures()
    
    