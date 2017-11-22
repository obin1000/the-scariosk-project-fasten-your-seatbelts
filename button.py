import RPi.GPIO as GPIO #Import library voor de pins op de raspberry pi

class button:
    
    GPIO.setmode(GPIO.BCM)                              #Gebruik de BCM nummering van de raspberrypi pins 
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Set pin 12 als een input en enable de ingebouwde weerstand om kortsluitng te voorkomen
    GPIO.add_event_detect(18, GPIO.RISING)              #Aanmaak detector voor response op pin 18
    
    def triggerButton(self):
        if GPIO.event_detected(18):
            return True
