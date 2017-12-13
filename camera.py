# sudo apt install python3-picamera
# sudo apt install python-picamera
import picamera #import benodigde libraries
from gpio import gpio

class foto:
    global camera
    camera = picamera.PiCamera() # Variable voor camera object
    path = '/home/pi/Pictures/'  # Standaart opslag locatie van de foto
    pixelsH = 1920               # Horizontaal aantal pixels van de foto
    pixelsV = 1080               # Verticaal aantal pixels van de foto
    rotatieH = False
    rotatieV = False
#    framerate = 30
    
    def savePath(self, pad):
        global path
        self.path = pad
        
##    def savePath(self, frames):
##        global framerate
##        self.framerate = frames
        
    def saveResolutie(self, horizontaal, verticaal):
        global pixelsH
        global pixelsV
        self.pixelsH = horizontaal
        self.pixelsV = verticaal
        
    def saveRotation(self, horizontaal, verticaal):
        global rotatieH
        global rotatieV
        self.rotatieH = horizontaal
        self.rotatieV = verticaal
        
    def setupCamera(self):
        camera.resolution = (self.pixelsH, self.pixelsV)
        camera.hflip = self.rotatieH
        camera.vflip = self.rotatieV
        #camera.framerate = self.framerate
        
    def takePictures(self, code, number):
        gpio().flitsAan()
        camera.capture_sequence([
            '{}{}{}.jpg'.format(self.path, code, count)
            for count in range(number)
            ], use_video_port=True)
        gpio().flitsUit()
        print('done')
            
            
            