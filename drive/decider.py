from config.config import config
from pubsub import pub

class decider:
    def __init__(self):
        pub.subscribe(self._rangeListener, 'curRangeFront')

    def _evadeObject(self):
        pub.sendMessage('moveDirection', moveDirection='left')
        pub.sendMessage('requestRange', rangeRequest=True)

    def _rangeListener(self, curRangeFront=0):
        print("listener for curRangeFront fired")
        if curRangeFront <= 15:
            self._evadeObject()

        else:
            pub.sendMessage('moveDirection', moveDirection='forward')