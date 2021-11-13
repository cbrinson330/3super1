from sensors import range

if __name__ == "__main__":
    """ init range sensor """
    rangeObj = range.range()

    while True:
        """ Check for ultrasonic sensor """
        rangeObj.takeReading()