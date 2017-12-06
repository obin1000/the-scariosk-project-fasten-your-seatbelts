import picamera #import benodigde libraries
class foto:
    global camera
    camera = picamera.PiCamera() # Variable voor camera object
    path = '/home/pi/Pictures/'  # Standaart opslag locatie van de foto
    pixelsH = 1920               # Horizontaal aantal pixels van de foto
    pixelsV = 1080               # Verticaal aantal pixels van de foto
    rotatieH = False
    rotatieV = False
    
    def savePath(self, pad):
        global path
        self.path = pad
        
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
        
    def takePictures(self, code, number):
        #loop voor het maken van meerdere fotos
        for count in range (0 , number):
            camera.capture('{}{}{}.jpg'.format(self.path, code, count))
            print('pic {}'.format(count))