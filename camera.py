import picamera
class foto:
    
    def saveResolutie(self, horizontaal, verticaal):
        self.pixelsH = horizontaal
        self.pixelsV = verticaal
        
        
    def takePictures(self):
        camera = picamera.PiCamera()
        camera.resolution = (self.pixelsH, self.pixelsV)
        #camera.hflip = rotatieHorizontaal
        #camera.vflip = rotatieVerticaal
        print(self.pixelsH + self.pixelsV)
        #loop voor het maken van 6 burst fotos
        for count in range (0 , 6):
            camera.capture('/home/pi/Downloads/'+str(count+1)+'.jpg')
            #print dat de foto genomen is
            print('picture ' + str(count+1) + ' taken!')

