from Libraries.IO_definitions.IO_definitions import *
import other_definitions

def motor_on():
    other_definitions.motor_running=1
    high(relay_MOTOR)
    sleep(other_definitions.DELAY_MOTOR_ON)

def motor_off():
    low(relay_MOTOR)
    other_definitions.motor_running=0
    sleep(other_definitions.DELAY_MOTOR_OFF)