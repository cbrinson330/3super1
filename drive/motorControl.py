from pubsub import pub
import RPi.GPIO as GPIO          
import time

class motorControl:
    def __init__(self):
        """ TODO setup here """
        print("init motor control")
        pub.subscribe(self._listener, 'moveDirection')

        GPIO.setmode(GPIO.BCM)

        # Left Motor 
        self.in1 = 24
        self.in2 = 23
        self.en = 25
        GPIO.setup(self.in1,GPIO.OUT)
        GPIO.setup(self.in2,GPIO.OUT)
        GPIO.setup(self.en,GPIO.OUT)
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.LOW)

        # Right Motor
        """
        self.in3 = 17 
        self.in4 = 27
        self.enR = 22
        GPIO.setup(self.in3,GPIO.OUT)
        GPIO.setup(self.in4,GPIO.OUT)
        GPIO.setup(self.enR,GPIO.OUT)
        GPIO.output(self.in3,GPIO.LOW)
        GPIO.output(self.in4,GPIO.LOW)
        pR=GPIO.PWM(self.enR,1000)
        pR.start(25)
        """

    def _listener(self, moveDirection=""):
        self._left()
        """ 
        if moveDirection == "forward":
            self._forward()
        elif moveDirection == "reverse":
            self._reverse()
        elif moveDirection == "left":
            self._left()
        elif moveDirection == "right":
            self._right()
        """
    """
    def _forward(self):
        print("Move Forward")
        # Left wheel
        GPIO.output(self.in1,GPIO.HIGH)
        GPIO.output(self.in2,GPIO.LOW)
        # Right Wheel
        GPIO.output(self.in3,GPIO.HIGH)
        GPIO.output(self.in4,GPIO.LOW)

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
    """
    def _left(self):
        print("Move left")
        # Left wheel
        p=GPIO.PWM(self.en,1000)
        p.start(25)
        GPIO.output(self.in1,GPIO.HIGH)
        GPIO.output(self.in2,GPIO.LOW)
        time.sleep(3)
        # Right Wheel
        # GPIO.output(self.in3,GPIO.LOW)
        # GPIO.output(self.in4,GPIO.HIGH)
    """
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
    """
