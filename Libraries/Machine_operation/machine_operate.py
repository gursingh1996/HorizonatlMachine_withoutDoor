import threading
from . import readButtons
import time

def machineOperate():
    while(1):
        readButtons.start()
        readButtons.bail_plate_down()
        print("Thread started")
        time.sleep(1)

def start_machineOperate_thread(self):
        thread = threading.Thread(target=machineOperate)
        thread.daemon = 1
        thread.start()