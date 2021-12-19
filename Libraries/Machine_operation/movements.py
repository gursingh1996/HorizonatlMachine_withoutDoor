import other_definitions
from Libraries.IO_definitions.IO_definitions import *
import motor_control
import condition_checker

def apply_lock():
    if not read(limit_LOCK_applied):
        high(coil_LOCK_applied)
        while not read(limit_LOCK_applied):
            fault = condition_checker.runningConditions(other_definitions.LOCK_APPLY)
            if fault == other_definitions.reset_pressed:        
                low(coil_LOCK_applied)              #upper plate down coil will turn off when funtion's value is returned
                sleep(other_definitions.DELAY_OPERATION)
                motor_control.motor_off()
                return fault
            
            low(coil_LOCK_applied)
            sleep(other_definitions.DELAY_OPERATION)

        return other_definitions.all_ok

def bring_upper_plate_forward_and_apply_lock():
    if not read(limit_UPPER_PLATE_fordward):     #confirm that upper plate is not already down
        if not other_definitions.motor_running: motor_control.motor_on() 
        high(coil_UPPER_PLATE_fordward)
        while not read(limit_UPPER_PLATE_fordward): #till limit is not pressed
            fault = condition_checker.runningConditions(other_definitions.UPPER_PLATE_forward)
            if fault==other_definitions.upper_plate_forward_pressure_reached:
                low(coil_UPPER_PLATE_fordward)
                sleep(other_definitions.DELAY_OPERATION)
                return fault
            
            elif fault==other_definitions.reset_pressed:
                low(coil_UPPER_PLATE_fordward)
                sleep(other_definitions.DELAY_OPERATION)
                motor_control.motor_off()
                return fault
        
        fault = apply_lock()
        low(coil_UPPER_PLATE_fordward)
        sleep(other_definitions.DELAY_OPERATION)
        if fault != other_definitions.all_ok: return fault
        return other_definitions.all_ok

    if not read(limit_LOCK_applied):
        if not other_definitions.motor_running: motor_control.motor_on()
        high(coil_UPPER_PLATE_fordward)
        sleep(other_definitions.DELAY_OPERATION)
        fault = apply_lock()
        low(coil_UPPER_PLATE_fordward)
        sleep(other_definitions.DELAY_OPERATION)
        if fault != other_definitions.all_ok: return fault
        return other_definitions.all_ok
    
    return other_definitions.all_ok

def bring_UPPER_PLATE_little_back():
    if not read(limit_UPPER_PLATE_back):        #upper plate should not be at the starting position
        milliSecCounter=0                       #no need to turn on the motor as this funtion will always run within other function
        high(coil_UPPER_PLATE_backward)
        while not read(limit_UPPER_PLATE_back):
            sleep(0.001)
            milliSecCounter+=1
            if milliSecCounter>=500: break        #run backward only for 500 milli seconds
            fault = condition_checker.runningConditions(other_definitions.UPPER_PLATE_back)
            if milliSecCounter>300 and fault == other_definitions.upper_plate_back_pressure_reached: break      #check pressure after 300 milli seconds
            elif fault == other_definitions.reset_pressed:
                low(coil_UPPER_PLATE_backward)
                sleep(other_definitions.DELAY_OPERATION)
                motor_control.motor_off()
                return other_definitions.reset_pressed
            
        low(coil_UPPER_PLATE_backward)
        sleep(other_definitions.DELAY_OPERATION)

    return other_definitions.all_ok


def normalStart(startFrom):
    go_on=0
    if startFrom == other_definitions.UPPER_PLATE_press_budle:
        retry=0
        for retry in range(3):      #retry three times only
            condition = bring_upper_plate_forward_and_apply_lock()
            if condition==other_definitions.reset_pressed:
                stopped_with_reset=1
                return other_definitions.UPPER_PLATE_press_budle

