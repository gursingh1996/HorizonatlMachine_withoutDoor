import threading
import RPi.GPIO as GPIO
from time import sleep

class inputExpander():
    CLKINH = 19
    SH = 6
    CLK = 13
    DATA = 26
    def init(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(inputExpander.CLKINH, GPIO.OUT)
        GPIO.setup(inputExpander.SH, GPIO.OUT)
        GPIO.setup(inputExpander.CLK, GPIO.OUT)
        GPIO.setup(inputExpander.DATA,GPIO.IN)

        GPIO.output(inputExpander.CLKINH, GPIO.HIGH)
        GPIO.output(inputExpander.SH, GPIO.HIGH)
        GPIO.output(inputExpander.CLK, GPIO.LOW)
        sleep(1)

    def readDataThread(self):
        while True:
            GPIO.output(inputExpander.SH, GPIO.LOW)
            sleep(0.001)
            GPIO.output(inputExpander.SH, GPIO.HIGH)
            sleep(0.001)
            GPIO.output(inputExpander.CLKINH, GPIO.LOW)
            sleep(0.001)
            if GPIO.input(inputExpander.DATA):
                print("1: 1")
            else:
                print("1: 0")
                
            for i in range(7):
                GPIO.output(inputExpander.CLK, GPIO.HIGH)
                sleep(0.001)
                if GPIO.input(inputExpander.DATA):
                    print(str(i+2)+": 1")
                else:
                    print(str(i+2)+": 0")
                    
                GPIO.output(inputExpander.CLK, GPIO.LOW)
                sleep(0.001)
                
            GPIO.output(inputExpander.CLKINH, GPIO.LOW)
            sleep(1)
            print("Done")

    def readDataLoop(self):
        thread = threading.Thread(target=self.readDataThread)
        thread.daemon = 1
        thread.start()