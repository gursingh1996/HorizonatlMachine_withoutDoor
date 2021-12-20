import threading
import RPi.GPIO as GPIO
from time import sleep
from tkinter import *

machineOutputs = [0]*16

def init_outputExpander(self, OE, SER, SRCLK, RCLK):
    self.OE = OE
    self.SER = SER
    self.SRCLK = SRCLK
    self.RCLK = RCLK
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.OE, GPIO.OUT)
    GPIO.setup(self.SER, GPIO.OUT)
    GPIO.setup(self.SRCLK, GPIO.OUT)
    GPIO.setup(self.RCLK,GPIO.OUT)

def writeOutputs():
    pass

    