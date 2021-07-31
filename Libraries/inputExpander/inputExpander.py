import threading
import RPi.GPIO as GPIO
from time import sleep

machineInputs = ['0']*8

class inputExpander():
    CLKINH = 19
    SH = 6
    CLK = 13
    DATA = 26
    def __init__(self):
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
        tempInputs = ['0']*8
        while True:
            GPIO.output(inputExpander.SH, GPIO.LOW)
            sleep(0.001)
            GPIO.output(inputExpander.SH, GPIO.HIGH)
            sleep(0.001)
            GPIO.output(inputExpander.CLKINH, GPIO.LOW)
            sleep(0.001)
            if GPIO.input(inputExpander.DATA):
                print("1: 1")
                tempInputs[0] = '1'
            else:
                print("1: 0")
                tempInputs[0] = '0'
                
            for i in range(7):
                GPIO.output(inputExpander.CLK, GPIO.HIGH)
                sleep(0.001)
                if GPIO.input(inputExpander.DATA):
                    print(str(i+2)+": 1")
                    tempInputs[i+1] = '1'
                else:
                    print(str(i+2)+": 0")
                    tempInputs[i+1] = '0'
                    
                GPIO.output(inputExpander.CLK, GPIO.LOW)
                sleep(0.001)
                
            GPIO.output(inputExpander.CLKINH, GPIO.LOW)
            inputExpander.machineInputs = tempInputs
            sleep(1)
            print("Done")

    def readDataLoop(self):
        thread = threading.Thread(target=self.readDataThread)
        thread.daemon = 1
        thread.start()

class InputIconsDisplay():
    def __init__(self, iconLabels, iconUnpressed, iconPressed):
        self.iconLabels = iconLabels
        self.iconUnpressed = iconUnpressed      #stores image data of icon
        self.iconPressed = iconPressed

    def changeIconsWithInputsLoop(self):
        thread = threading.Thread(target=self.changeIconsWithInputs)
        thread.daemon = 1
        thread.start()

    def changeIconsWithInputs(self):
        for i in range(8):
            if machineInputs[i]=='0':
                self.iconLabels = self.iconUnpressed
            else:
                self.iconLabels = self.iconPressed
