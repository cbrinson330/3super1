from sensors import range
from drive import decider
from drive import motorControl
import time

if __name__ == "__main__":
    """ init classes """
    rangeObj = range.range()
    deciderObj = decider.decider()
    motorControl = motorControl.motorControl()

    while True:
        """ Check for ultrasonic sensor """
        rangeObj.takeReading()
        time.sleep(2)