#!/usr/bin/python3
#
# http://jheyman.github.io/blog/pages/HueRaspberryControl/
# https://github.com/armzilla/amazon-echo-ha-bridge
#
#
#
#
#


from time import sleep
from phue import Bridge

ip_of_hue_bridge = "192.168.2.115"

b = Bridge(ip_of_hue_bridge)

#result = b.get_light(2, 'on')

#print "light 2 is " + str(result)

#result = b.get_api()
#print result

#b.set_light(3, 'bri', 254)

#b.set_light(3, 'hue', 50000)
# Get a dictionary with the light id as the key
lights = b.get_light_objects('id')

print ("1 reac: " + str(lights[1].reachable))
print ("name: " + str(lights[1].name))
print ("")

# Get the name of light 1, set the brightness to 127  reachable
print ("name: " + str(lights[3].name))
print ("reac: " + str(lights[3].reachable))
print ("on  : " + str(lights[3].on))
print ("hue : " + str(lights[3].hue))
print ("bri : " + str(lights[3].brightness))
print ("sat : " + str(lights[3].saturation))

#lights[3].name = 'Stairs'
lights[3].brightness = 135
lights[3].hue = 27926
lights[3].saturation = 216

#lights[2].name = 'UpperHallRight'
lights[2].brightness = 135
lights[2].hue = 27926
lights[2].saturation = 216

#lights[1].name = 'Bedroom'
#lights[1].brightness = 135
#lights[1].hue = 27926
#lights[1].saturation = 216

# Get a dictionary with the light name as the key
light_names = b.get_light_objects('name')
#print "---light_names---"
#print light_names
#print lights

light_names["Bedroom"].brightness = 135
light_names["Bedroom"].hue = 0
light_names["Bedroom"].saturation = 216

for light in ['Salon Stand 1', 'Salon Stand 2', 'Salon Stand 3']:
    light_names[light].on = True
    light_names[light].hue = 27926
    light_names[light].saturation = 254

#for i in xrange(30):
#   light_names["Stairs"].hue = 0
#   sleep(1.0) # Time in seconds.
#   light_names["Stairs"].hue = 25500
#   sleep(1.0) # Time in seconds.

#for light in ['Stairs', 'UpperHallRight']:
#    light_names[light].on = False


   