import other_definitions
from Libraries.IO_definitions.IO_definitions import *
import parameters

def startingCondition():
    if not read(limit_BAIL_PLATE_down):		#if bail plate is not down
        return other_definitions.BAIL_PLATE_not_down
    
    elif not read(limit_LOWER_PLATE_back):
        return other_definitions.LOWER_PLATE_not_back

    elif not read(limit_LOCK_out):		#if lock is not in initial position
        return other_definitions.lock_not_out
    
    elif not read(limit_UPPER_PLATE_back):		#if upper plate is not in initial position
        return other_definitions.UPPER_PLATE_not_up

    return other_definitions.all_ok		#if every thing is fine return ok


def runningConditions(operation):
    if read(btn_RESET): return other_definitions.reset_pressed

    if operation == other_definitions.UPPER_PLATE_forward:
        if other_definitions.pressureSense >= parameters.UPPER_PLATE_forward_pressure:
            return other_definitions.upper_plate_forward_pressure_reached
        
    elif operation == other_definitions.LOWER_PLATE_backward:
        if other_definitions.pressureSense >= parameters.LOWER_PLATE_backward_pressure:
            return other_definitions.lower_plate_back_pressure_reached

    elif operation == other_definitions.LOCK_OUT:
        return 0
    
    elif operation == other_definitions.UPPER_PLATE_back:
        if other_definitions.pressureSense >= parameters.UPPER_PLATE_backward_pressure:
            return other_definitions.upper_plate_back_pressure_reached

    elif operation == other_definitions.LOCK_APPLY:
        return 0

    elif operation == other_definitions.LOWER_PLATE_forward:
        return 0
    
    elif operation == other_definitions.BALE_PLATE_up:
        return 0

    elif operation == other_definitions.BALE_PLATE_down:
        return 0

    return 0