from camera import foto
from button import button

if __name__ == "__main__":
    knop = button()
    maakFoto = foto()
    maakFoto.saveResolutie(1920,1080)
    
    while True:
        if knop.triggerButton():
            maakFoto.takePictures()
    
    