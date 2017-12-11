import RPi.GPIO as GPIO #Import library voor de pins op de raspberry pi

class gpio:
    
    GPIO.setmode(GPIO.BOARD)                            #Gebruik de BOARD nummering van de raspberrypi pins 
    GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Set pin 18 als een input en enable de ingebouwde weerstand om kortsluitng te voorkomen
    GPIO.setup(18, GPIO.OUT)
    GPIO.add_event_detect(12, GPIO.RISING)              #Aanmaak detector voor response op pin 18

    
    def triggerButton(self):
        if GPIO.event_detected(12):
            return True
        
    def flitsAan(self):
        GPIO.output(18,1)
        
    def flitsUit(self):
        GPIO.output(18,0)
        
        

        
        

