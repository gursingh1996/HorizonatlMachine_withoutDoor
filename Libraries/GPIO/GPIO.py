import threading
import RPi.GPIO as GPIO

inputPin = 9

class GPIOPins():
    def initPins(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(inputPin,GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def readPin(self):
        while True:
            if not GPIO.input(inputPin):
                print("detected")

    def beginReading(self):
        thread = threading.Thread(target=self.readPin)
        thread.daemon = 1
        thread.start()
        
        
        
        