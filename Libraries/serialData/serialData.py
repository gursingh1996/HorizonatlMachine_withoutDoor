import threading
from time import sleep

timing = 0

class serialData():
    def dataLoop(self):
        while(1):
            global timing
            timing+=1
            print("time is: "+ str(timing))
            sleep(1)

    def initLoop(self):
        thread = threading.Thread(target=self.dataLoop)
        thread.daemon = 1
        thread.start()