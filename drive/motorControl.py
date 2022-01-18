from pubsub import pub
import RPi.GPIO as GPIO          
import time

class motorControl:
    def __init__(self):
        """ TODO setup here """
        print("init motor control")
        pub.subscribe(self._listener, 'moveDirection')
        GPIO.setmode(GPIO.BCM)

        self.turnTime = 3
        self.moveTime = 1

        # Left Motor 
        self.in1 = 24
        self.in2 = 23
        self.enL = 25
        GPIO.setup(self.in1,GPIO.OUT)
        GPIO.setup(self.in2,GPIO.OUT)
        GPIO.setup(self.enL,GPIO.OUT)
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.LOW)

        # Right Motor
        self.in3 = 17 
        self.in4 = 27
        self.enR = 22
        GPIO.setup(self.in3,GPIO.OUT)
        GPIO.setup(self.in4,GPIO.OUT)
        GPIO.setup(self.enR,GPIO.OUT)
        GPIO.output(self.in3,GPIO.LOW)
        GPIO.output(self.in4,GPIO.LOW)

    def _listener(self, moveDirection=""):
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
        # Left wheel
        pL=GPIO.PWM(self.enL,1000)
        pL.start(50)
        GPIO.output(self.in1,GPIO.HIGH)
        GPIO.output(self.in2,GPIO.LOW)
        # Right Wheel
        pR=GPIO.PWM(self.enR,1000)
        pR.start(50)
        GPIO.output(self.in3,GPIO.HIGH)
        GPIO.output(self.in4,GPIO.LOW)
        time.sleep(self.moveTime)

    def _reverse(self):
        print("Move backwards")
        # Left wheel
        pL=GPIO.PWM(self.enL,1000)
        pL.start(50)
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.HIGH)
        # Right Wheel
        pR=GPIO.PWM(self.enR,1000)
        pR.start(50)
        GPIO.output(self.in3,GPIO.LOW)
        GPIO.output(self.in4,GPIO.HIGH)
        time.sleep(self.moveTime)

    def _left(self):
        print("Move left")
        # Left wheel
        pL=GPIO.PWM(self.enL,1000)
        pL.start(50)
        GPIO.output(self.in1,GPIO.HIGH)
        GPIO.output(self.in2,GPIO.LOW)
        # Right Wheel
        pR=GPIO.PWM(self.enR,1000)
        pR.start(50)
        GPIO.output(self.in3,GPIO.LOW)
        GPIO.output(self.in4,GPIO.HIGH)
        # Time to perform left turn
        time.sleep(self.turnTime)

    def _right(self):
        print("Move left")
        # Left wheel
        pL=GPIO.PWM(self.enL,1000)
        pL.start(50)
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.HIGH)
        # Right Wheel
        pR=GPIO.PWM(self.enR,1000)
        pR.start(50)
        GPIO.output(self.in3,GPIO.HIGH)
        GPIO.output(self.in4,GPIO.LOW)
        # Time to perform left turn
        time.sleep(self.turnTime)