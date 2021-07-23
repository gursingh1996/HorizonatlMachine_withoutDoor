import threading
import RPi.GPIO as GPIO
from time import sleep

class inputExpander():
    clkinh = 4
    sh = 17
    clk = 27
    qh = 22
    def init(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(inputExpander.clkinh, GPIO.OUT)
        GPIO.setup(inputExpander.sh, GPIO.OUT)
        GPIO.setup(inputExpander.clk, GPIO.OUT)
        GPIO.setup(inputExpander.qh,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        GPIO.output(inputExpander.clkinh, GPIO.HIGH)
        GPIO.output(inputExpander.sh, GPIO.HIGH)
        GPIO.output(inputExpander.clk, GPIO.LOW)

    def readDataThread(self):
        while True:
            receivedData = ''
            GPIO.output(inputExpander.sh, GPIO.LOW)
            sleep(0.01)
            GPIO.output(inputExpander.sh, GPIO.HIGH)
            sleep(0.01)
            GPIO.output(inputExpander.clkinh, GPIO.LOW)
            sleep(0.01)
            for i in range(8):
                GPIO.output(inputExpander.clk, GPIO.HIGH)
                sleep(0.01)
                if GPIO.input(inputExpander.qh):
                    receivedData += '1'
                else:
                    receivedData += '0'
                GPIO.output(inputExpander.clk, GPIO.LOW)
                sleep(0.01)

            GPIO.output(inputExpander.clkinh, GPIO.HIGH)
            print(receivedData)
            sleep(1)

    def readDataLoop(self):
        thread = threading.Thread(target=self.readDataThread)
        thread.daemon = 1
        thread.start()
