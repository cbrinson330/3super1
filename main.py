from sensors import range
from drive import decider
from drive import motorControl
from tests import motorTest
import sys
import time
import RPi.GPIO as GPIO

if __name__ == "__main__":
    GPIO.setwarnings(False);

    """ init classes """
    rangeObj = range.range()
    deciderObj = decider.decider()
    motorControl = motorControl.motorControl()

    """ check if test param passed """
    if len(sys.argv) > 1:

        """ Handle args """
        if str(sys.argv[1]) == 'runTests':
            print ('Running motor Tests')
            motorTestObj = motorTest.motorTest()

    else:
       while True:
           """ Check for ultrasonic sensor """
           rangeObj.takeReading()
           time.sleep(2)
