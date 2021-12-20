import warning
import function_number
import parameters
import variables
from Libraries.IO_definitions.IO_definitions import *
import motor_control
import condition_checker

def bring_upper_plate_forward_and_apply_lock():
    if not read(limit_UPPER_PLATE_fordward):     #confirm that upper plate is not already down
        if not variables.motor_running: motor_control.motor_on() 
        high(coil_UPPER_PLATE_fordward)
        while not read(limit_UPPER_PLATE_fordward): #till limit is not pressed
            fault = condition_checker.runningConditions(function_number.UPPER_PLATE_forward)
            if fault==warning.upper_plate_forward_pressure_reached:
                low(coil_UPPER_PLATE_fordward)
                sleep(parameters.DELAY_OPERATION)
                return fault
            
            elif fault==warning.reset_pressed:
                low(coil_UPPER_PLATE_fordward)
                sleep(parameters.DELAY_OPERATION)
                motor_control.motor_off()
                return fault
        
        fault = apply_lock()
        low(coil_UPPER_PLATE_fordward)
        sleep(parameters.DELAY_OPERATION)
        if fault != warning.all_ok: return fault
        return warning.all_ok

    if not read(limit_LOCK_applied):
        if not variables.motor_running: motor_control.motor_on()
        high(coil_UPPER_PLATE_fordward)
        sleep(parameters.DELAY_OPERATION)
        fault = apply_lock()
        low(coil_UPPER_PLATE_fordward)
        sleep(parameters.DELAY_OPERATION)
        if fault != warning.all_ok: return fault
        return warning.all_ok
    
    return warning.all_ok

def apply_lock():
    if not read(limit_LOCK_applied):
        high(coil_LOCK_applied)
        while not read(limit_LOCK_applied):
            fault = condition_checker.runningConditions(function_number.LOCK_APPLY)
            if fault == warning.reset_pressed:        
                low(coil_LOCK_applied)              #upper plate down coil will turn off when funtion's value is returned
                sleep(parameters.DELAY_OPERATION)
                motor_control.motor_off()
                return fault
            
            low(coil_LOCK_applied)
            sleep(parameters.DELAY_OPERATION)

        return warning.all_ok

def bring_UPPER_PLATE_little_back():
    if not read(limit_UPPER_PLATE_back):        #upper plate should not be at the starting position
        milliSecCounter=0                       #no need to turn on the motor as this funtion will always run within other function
        high(coil_UPPER_PLATE_backward)
        while not read(limit_UPPER_PLATE_back):
            sleep(0.001)
            milliSecCounter+=1
            if milliSecCounter>=500: break        #run backward only for 500 milli seconds
            fault = condition_checker.runningConditions(function_number.UPPER_PLATE_back)
            if milliSecCounter>300 and fault == warning.upper_plate_back_pressure_reached: break      #check pressure after 300 milli seconds
            elif fault == warning.reset_pressed:
                low(coil_UPPER_PLATE_backward)
                sleep(parameters.DELAY_OPERATION)
                motor_control.motor_off()
                return warning.reset_pressed
            
        low(coil_UPPER_PLATE_backward)
        sleep(parameters.DELAY_OPERATION)

    return warning.all_ok


def bring_lower_plate_forward():        #no starting conditions need to be checked
    if not variables.motor_running: motor_control.motor_on()
    high(coil_LOWER_PLATE_fordward)
    while True:
        fault = condition_checker.runningConditions(function_number.LOWER_PLATE_forward)
        if fault == warning.lower_plate_forward_pressure_reached: break
        elif fault == warning.reset_pressed:
            low(coil_LOWER_PLATE_fordward)
            sleep(parameters.DELAY_OPERATION)
            motor_control.motor_off()
            return warning.reset_pressed
        
    low(coil_LOWER_PLATE_fordward)
    sleep(parameters.DELAY_OPERATION)
    return warning.all_ok

def bring_lower_plate_back():
    if not read(limit_LOWER_PLATE_back):
        if not variables.motor_running: motor_control.motor_on()
        milliSecCounter=0
        high(coil_LOWER_PLATE_backward)
        while not read(limit_LOWER_PLATE_back):
            if milliSecCounter<500:
                sleep(0.001)
                milliSecCounter+=1

            fault = condition_checker.runningConditions(function_number.LOWER_PLATE_backward)
            if milliSecCounter==500 and fault == warning.lower_plate_back_pressure_reached: break #check pressure after 500 ms
            elif fault == warning.reset_pressed:
                low(coil_LOWER_PLATE_backward)
                sleep(parameters.DELAY_OPERATION)
                motor_control.motor_off()
                return fault
            
        low(coil_LOWER_PLATE_backward)
        sleep(parameters.DELAY_OPERATION)

    return warning.all_ok

def bring_lock_out():           #pressure not checked here
    if not read(limit_LOCK_out):
        if not variables.motor_running: motor_control.motor_on()
        milliSecCounter=0
        high(coil_UPPER_PLATE_fordward)
        while not read(limit_LOCK_out):
            if milliSecCounter<500:
                sleep(0.001)
                milliSecCounter+=1
            
            if milliSecCounter==500:
                milliSecCounter+=1      #so that this condition doesnot run forever
                high(coil_LOCK_out)     #turn on lock out coil after 500 ms after coil upper plate forward
            
            fault = condition_checker.runningConditions(function_number.LOCK_OUT)
            if fault == warning.reset_pressed:
                low(coil_LOCK_out)
                low(coil_UPPER_PLATE_fordward)
                sleep(parameters.DELAY_OPERATION)
                motor_control.motor_off()
                return fault
        
        low(coil_LOCK_out)
        low(coil_UPPER_PLATE_fordward)

    return warning.all_ok

def bring_upper_plate_back():
    if not read(limit_UPPER_PLATE_back):
        if not variables.motor_running: motor_control.motor_on()
        milliSecCounter=0
        high(coil_UPPER_PLATE_backward)
        while not read(limit_UPPER_PLATE_back):
            if milliSecCounter<500:
                sleep(0.001)
                milliSecCounter+=1
            
            fault = condition_checker.runningConditions(function_number.UPPER_PLATE_back)
            if milliSecCounter==500 and warning.upper_plate_back_pressure_reached: break
            elif fault == warning.reset_pressed:
                low(coil_UPPER_PLATE_backward)
                sleep(parameters.DELAY_OPERATION)
                motor_control.motor_off()
                return fault

        low(coil_UPPER_PLATE_backward)
        sleep(parameters.DELAY_OPERATION)
    
    return warning.all_ok

def bring_bail_plate_up():
    if read(limit_UPPER_PLATE_back) and read(limit_LOWER_PLATE_back):
        if not variables.motor_running: motor_control.motor_on()
        high(coil_BAIL_PLATE_up)
        milliSecCounter=0
        while milliSecCounter<3000:     #work for 3 seconds
            sleep(0.001)
            milliSecCounter+=1
            fault = condition_checker.runningConditions(function_number.BALE_PLATE_up)
            if fault == warning.bale_plate_up_pressure_reached: break
            elif fault == warning.reset_pressed:
                low(coil_BAIL_PLATE_up)
                sleep(parameters.DELAY_OPERATION)
                motor_control.motor_off()
                return fault

        low(coil_BAIL_PLATE_up)
        sleep(parameters.DELAY_OPERATION)
    
    return warning.all_ok

def bring_bail_plate_down():
    if not read(limit_BAIL_PLATE_down):
        wait_time=0
        if not variables.motor_running: motor_control.motor_on()
        high(coil_BAIL_PLATE_down)
        while wait_time<750:        #press down for 750 milli seconds more
            if read(limit_BAIL_PLATE_down):
                sleep(0.001)
                wait_time+=1
            
            fault = condition_checker.runningConditions(function_number.BALE_PLATE_down)
            if fault == warning.bale_plate_down_pressure_reached: break
            elif fault == warning.reset_pressed:
                low(coil_BAIL_PLATE_down)
                sleep(parameters.DELAY_OPERATION)
                motor_control.motor_off()
                return fault
        
        low(coil_BAIL_PLATE_down)
        sleep(parameters.DELAY_OPERATION)
    
    return warning.all_ok


def normalStart(startFrom):
    go_on=0
    if startFrom == function_number.UPPER_PLATE_press_budle:
        retry=0
        for retry in range(3):      #try pressing the bundle three times only
            condition = bring_upper_plate_forward_and_apply_lock()
            if condition==warning.reset_pressed:
                stopped_with_reset=1
                return function_number.UPPER_PLATE_press_budle

            elif condition==warning.all_ok: pass      #go to next operation if this is success


