from sensors import range
from drive import decider
from drive import motorControl
from tests import motorTest
import sys
import time

if __name__ == "__main__":
    """ check if test param passed """
    if str(sys.argv[1]) == 'runTests':
        print('Running motor Tests')
        motorTest = motorTest.motorTest
        motorTest.runTests

    """ init classes """
    rangeObj = range.range()
    deciderObj = decider.decider()
    motorControl = motorControl.motorControl()

    while True:
        """ Check for ultrasonic sensor """
        rangeObj.takeReading()
        time.sleep(2)