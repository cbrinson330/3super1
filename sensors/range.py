from config import config
from pubsub import pub

class range:
    def __init__(self):
        print("init range")
        pub.subscribe(self._requestHandler, 'rangeRequest')
    
    def _determineSpeedOfSound(self):
        """ 
            TODO use temp and humidity to calculate the speed of sound
            to better calibrate range sensor
        """

    def _requestHandler(self, rangeRequest=True):
        if(rangeRequest):
            self.takeReading()

    def takeReading(self):
        print("Take range reading")
        pub.sendMessage('curRangeFront', curRangeFront=20)