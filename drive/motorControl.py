from config import config
from pubsub import pub

class motorControl:
    def __init__(self):
        """ TODO setup here """
        print("init motor control")
        pub.subscribe(self._listener, 'moveDirection')

    def _listener(self, moveDirection=""):
        """ TODO listener """
        if moveDirection == "forward":
            self._forward()
        elif moveDirection == "reverse":
            self._reverse()
        elif moveDirection == "left":
            self._left()
        elif moveDirection == "right":
            self._right()

    def _forward(self):
        print("Move Forward")

    def _reverse(self):
        print("Move backwards")
    
    def _left(self):
        print("Move left")

    def _right(self):
        print("Move right")