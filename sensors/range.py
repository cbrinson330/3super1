from config import config
from pubsub import pub

class range:
    def __init__(self):
        """ TODO setup here """
        print("init range")
    
    def _determineSpeedOfSound(self):
        """ 
            TODO use temp and humidity to calculate the speed of sound
            to better calibrate range sensor
        """

    def takeReading(self):
        """ TODO get curent sensor reading """
        print("Take range reading")
        pub.sendMessage('curRangeFront', 15)