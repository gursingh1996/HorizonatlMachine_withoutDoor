import threading
from Machine_operation import readButtons

def machineOperate():
    while(1):
        readButtons.start()

def start_machineOperate_thread(self):
        thread = threading.Thread(target=machineOperate)
        thread.daemon = 1
        thread.start()