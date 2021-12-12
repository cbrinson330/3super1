from ..drive import motorControl
from pubsub import pub
from time import time

class motorTest:
    def __init__(self):
        self.runTests()

    def runTests(self):
        pub.sendMessage('moveDirection', moveDirection='left')
        time.delay(3000)
        pub.sendMessage('moveDirection', moveDirection='right')
        time.delay(3000)
        pub.sendMessage('moveDirection', moveDirection='forwards')
        time.delay(3000)
        pub.sendMessage('moveDirection', moveDirection='reverse')
        time.delay(3000)

if __name__ == "__main__":
    motorControl = motorControl.motorControl()
    test = motorTest()