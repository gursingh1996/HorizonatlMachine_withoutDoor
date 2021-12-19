from Libraries.IO_definitions.IO_definitions import *
from time import sleep

def start():
    if read(btn_START):
        i=0 
        for i in range(1000):
            sleep(0.001)
            if read(btn_START)==0:
                i=0
                break
        
        if i==999:      #return to default position
            pass

        else:       #normal start
            pass 