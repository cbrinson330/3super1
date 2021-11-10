# config
    -> holds config info for GPIO pins

# Main Loop
    check sensor to see if we are too close
        -> Publish "warning" stop override message
        -> https://thepihut.com/blogs/raspberry-pi-tutorials/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi
    check camera image
        -> Publish "roomImage" every "x" cycles publish room image for consumption
        -> "roomImage" passes string of location of latest file

# Determine Path
    -> Subscribes to "warning", "roomImage"
    -> Determines path to take
    -> https://github.com/The-Assembly/Obstacle_avoidance_opencv
    -> Outputs speed and direction of wheel turning

# Check Room
    -> Subscribes to "roomImage"
    -> Publiches to "roomIdentified" current room "String"
    -> processes image to determine current room

# Log Environmentals
    -> Subscribes to "roomIdentified"
    -> takes sensor readings and logs them

# Lights
    -> Subscribes to "roomIdentified", "warning", "move"
    -> outputs lights blinking etc.