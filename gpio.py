import RPi.GPIO as GPIO #Import library voor de pins op de raspberry pi

class gpio:
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(5, GPIO.OUT)
    GPIO.setup(3, GPIO.OUT)
    GPIO.add_event_detect(12, GPIO.RISING, bouncetime=500)
    
    def triggerButton(self):
        if GPIO.event_detected(12):
            return True
        
    def flitsAan(self):
        GPIO.output(18,1)
        
    def flitsUit(self):
        GPIO.output(18,0)
        
    def motorPause(self):
        GPIO.output(5,1)
        GPIO.output(3,1)
        
    def motorLanseer(self):
        GPIO.output(5,1)
        GPIO.output(3,0)
        
    def motorReset(self):
        GPIO.output(5,0)
        GPIO.output(3,1)
        
        
        
        

        
        

