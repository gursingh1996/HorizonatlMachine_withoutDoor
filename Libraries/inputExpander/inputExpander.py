import threading
import RPi.GPIO as GPIO
from time import sleep
from tkinter import *

machineInputs = [0]*16

class inputExpander():
    def __init__(self, CLKINH, SH, CLK, DATA):
        self.CLKINH = CLKINH
        self.SH = SH
        self.CLK = CLK
        self.DATA = DATA
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.CLKINH, GPIO.OUT)
        GPIO.setup(self.SH, GPIO.OUT)
        GPIO.setup(self.CLK, GPIO.OUT)
        GPIO.setup(self.DATA,GPIO.IN)

        GPIO.output(self.CLKINH, GPIO.HIGH)
        GPIO.output(self.SH, GPIO.HIGH)
        GPIO.output(self.CLK, GPIO.LOW)
        sleep(0.001)

    def __readInputsThread(self):
        global machineInputs
        while True:
            GPIO.output(self.SH, GPIO.LOW)
            sleep(0.001)
            GPIO.output(self.SH, GPIO.HIGH)
            sleep(0.001)
            GPIO.output(self.CLKINH, GPIO.LOW)
            sleep(0.001)
            if GPIO.input(self.DATA):
                machineInputs[0] = 1
            else:
                machineInputs[0] = 0
                
            for i in range(15):
                GPIO.output(self.CLK, GPIO.HIGH)
                sleep(0.001)
                if GPIO.input(self.DATA):
                    machineInputs[i+1] = 1
                else:
                    machineInputs[i+1] = 0
                    
                GPIO.output(self.CLK, GPIO.LOW)
                sleep(0.001)
                
            GPIO.output(self.CLKINH, GPIO.LOW)
            sleep(0.001)

    def startReadingInputs(self):
        thread = threading.Thread(target=self.__readInputsThread)
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
        while True:
            print(machineInputs)
            for i in range(8):
                if machineInputs[i]=='0':
                    self.iconLabels[i].config(image=self.iconUnpressed)
                    self.iconLabels[i].image = self.iconUnpressed
                else:
                    self.iconLabels[i].config(image=self.iconPressed)
                    self.iconLabels[i].image = self.iconPressed
            sleep(1)