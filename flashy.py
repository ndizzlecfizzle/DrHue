###
# Flashy
# 
# Make sure to `export` an enviroment variable BRIDGE_IP *BEFORE YOU RUN THE SCRIPT*.

import os
import random
from phue import Bridge

b = Bridge(os.environ.get('BRIDGE_IP'))
b.connect() # Make sure to be pressing the button on the bridge when this is run,
# it will save the auth token to your computer so you don't have to do it again

# Get an array of all lights
lights = b.lights

# For every light
for light in lights:
    light.on # Turn light on

# Loop forever
while true:
    # For every light
    for light in lights:
        light.hue = random.randint(0, 65535)
        light.saturation = random.randint(0, 255)
        light.brightness = random.randint(0, 255)
