import threading
import RPi.GPIO as gpio

inputPin = 9

class GPIO():
    def initPins():
        gpio.setmode(gpio.BCM)
        GPIO.setup(inputPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def readPin(self):
        while True:
            if gpio.input(inputPin):
                print("detected")

    def beginReading(self):
        thread = threading.Thread(target=self.readPin)
        thread.daemon = 1
        thread.start()