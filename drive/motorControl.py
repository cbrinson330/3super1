from pubsub import pub
import RPi.GPIO as GPIO          
from time import sleep

class motorControl:
    def __init__(self):
        """ TODO setup here """
        print("init motor control")
        pub.subscribe(self._listener, 'moveDirection')

        GPIO.setmode(GPIO.BCM)

        # Left Motor 
        self.in1 = 24
        self.in2 = 23
        self.enL = 25
        GPIO.setup(self.in1,GPIO.OUT)
        GPIO.setup(self.in2,GPIO.OUT)
        GPIO.setup(self.enL,GPIO.OUT)
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.LOW)
        self.pL=GPIO.PWM(self.enL,1000)

        # Right Motor
        self.in3 = 17 
        self.in4 = 27
        self.enR = 22
        GPIO.setup(self.in3,GPIO.OUT)
        GPIO.setup(self.in4,GPIO.OUT)
        GPIO.setup(self.enR,GPIO.OUT)
        GPIO.output(self.in3,GPIO.LOW)
        GPIO.output(self.in4,GPIO.LOW)
        self.pR=GPIO.PWM(self.enR,1000)


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
        # Left wheel
        GPIO.output(self.in1,GPIO.HIGH)
        GPIO.output(self.in2,GPIO.LOW)
        self.pL.start(25) #25=low 50=medium 75=high
        # Right Wheel
        GPIO.output(self.in3,GPIO.HIGH)
        GPIO.output(self.in4,GPIO.LOW)
        self.pR.start(25) #25=low 50=medium 75=high

    def _reverse(self):
        print("Move backwards")
        # Left wheel
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.HIGH)
        self.pL.start(25) #25=low 50=medium 75=high
        # Right Wheel
        GPIO.output(self.in3,GPIO.LOW)
        GPIO.output(self.in4,GPIO.HIGH)
        self.pR.start(25) #25=low 50=medium 75=high
    
    def _left(self):
        print("Move left")
        # Left wheel
        GPIO.output(self.in1,GPIO.HIGH)
        GPIO.output(self.in2,GPIO.LOW)
        self.pL.start(25) #25=low 50=medium 75=high
        # Right Wheel
        GPIO.output(self.in3,GPIO.LOW)
        GPIO.output(self.in4,GPIO.HIGH)
        self.pR.start(25) #25=low 50=medium 75=high

    def _right(self):
        print("Move right")
        # Left wheel
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.HIGH)
        self.pL.start(25) #25=low 50=medium 75=high
        # Right Wheel
        GPIO.output(self.in3,GPIO.HIGH)
        GPIO.output(self.in4,GPIO.LOW)
        self.pR.start(25) #25=low 50=medium 75=high
