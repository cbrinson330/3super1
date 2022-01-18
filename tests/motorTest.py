from drive import motorControl 
from pubsub import pub
import time
import sys

class motorTest:
    def __init__(self):
        self.runTests()

    def runTests(self):
        print('running motor tests')
        print('running motor left test')
        pub.sendMessage('moveDirection', moveDirection='left')
        #print('running motor right test')
        #pub.sendMessage('moveDirection', moveDirection='right')
        #time.sleep(3)
        #print('running motor forward test')
        #pub.sendMessage('moveDirection', moveDirection='forwards')
        #time.sleep(3)
        #print('running motor reverse test')
        #pub.sendMessage('moveDirection', moveDirection='reverse')
        #print('ending motor tests')

if __name__ == "__main__":
    motorControl = motorControl.motorControl()
    test = motorTest()
