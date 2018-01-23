import RPi.GPIO as GPIO #Import library voor de pins op de raspberry pi

class gpio:
    #Gebruik van de Board nummering op de pi
    GPIO.setmode(GPIO.BOARD)
    #Configureren van de pins naar input/ output
    GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(12, GPIO.RISING, bouncetime=500)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(5, GPIO.OUT)
    GPIO.setup(3, GPIO.OUT)
    
    #methode om te kijken of de knop is ingedrukt
    def triggerButton(self):
        if GPIO.event_detected(12):
            return True

    def flitsAan(self):
        GPIO.output(18,1)
    
    def flitsUit(self):
        GPIO.output(18,0)
        
    #zet de motor op een niet draaiende pauze stand
    def motorPause(self):
        GPIO.output(5,1)
        GPIO.output(3,1)
        
    #draait de motor rechtsom, om de spin te lanseren
    def motorLanseer(self):
        GPIO.output(5,1)
        GPIO.output(3,0)
    
    #draait de motor rechtsom, om de spin terug te trekken    
    def motorReset(self):
        GPIO.output(5,0)
        GPIO.output(3,1)
        
        
        
        

        
        

