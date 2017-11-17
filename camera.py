import picamera
from gpiozero import Button
from time import sleep
from random import randint

fotoknop = Button(23) <-- Verander waar je de button hebt ingeplugd
camera = picamera.PiCamera()
camera.resolution = (400, 800)
camera.vflip = True
camera.start_preview()
output = "foto/%d/%d.jpg" % (id, i) <-- Moet nog ff manier vinden om automatisch een map te maken

    
def foto():
    
    for i in range(0, 7):
        camera.capture(output)
        camera.stop_preview()
        sleep(1)
    
fotoknop.when_pressed = foto