from Libraries.inputExpander.inputExpander import *
from Libraries.outputExpander import outputExpander

#inputs
limit_UPPER_PLATE_fordward = 0
limit_UPPER_PLATE_back = 1
limit_LOWER_PLATE_back = 2			
btn_START = 3			
btn_RESET = 4					
btn_BALE_PLATE_down = 5			
limit_BAIL_PLATE_down = 6			
limit_LOCK_out = 7			
limit_LOCK_applied = 8				

#outputs
relay_MOTOR = 0
coil_LOWER_PLATE_fordward = 1
coil_LOWER_PLATE_backward = 2
coil_UPPER_PLATE_backward = 3 
coil_UPPER_PLATE_fordward = 4
coil_BAIL_PLATE_up = 5
coil_BAIL_PLATE_down = 6
coil_LOCK_applied = 7
coil_LOCK_out = 8

#Raspberry pi used pins
inputExpander_CLKINH = 19
inputExpander_SH = 6
inputExpander_CLK = 13
inputExpander_DATA = 26
#not defined
outputExpander_OE = 0
outputExpander_SER = 0
outputExpander_SRCLK = 0
soutputExpanderelf_RCLK = 0

def initIO():      #initialize inputs and outputs of the machine
    GPIO.setwarnings(False)
    inputs = inputExpander(inputExpander_CLKINH, inputExpander_SH, inputExpander_CLK, inputExpander_DATA)
    inputs.startReadingInputs()     #start the thread
    outputExpander.init_outputExpander(outputExpander_OE, outputExpander_SER, outputExpander_SRCLK, soutputExpanderelf_RCLK)

def read(pin):
    return machineInputs[pin]       #return value as integer

def high(pin):
    outputExpander.machineOutputs[pin] = 1
    outputExpander.writeOutputs()

def low(pin):
    outputExpander.machineOutputs[pin] = 0
    outputExpander.writeOutputs()