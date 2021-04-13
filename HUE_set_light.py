#!/usr/bin/python3
###############################################################################
#
# HUE_set_light.py : HUE set light
# --------------------------------
#
# system .............: linux
# directory ..........: 
# program ............: HUE_set_light.py
# version / release ..: 0.1
# date ...............: 2020.05.02 mg version 0.1
#
# programmer .........: Marcel Gross
# department .........: IT
#
# application group...: 
# application ........: mm_HUE : Philips HUE Lights
#
# usage ..............: HUE_set_light.py -l <lightName>
#                                        -S [on|off|query]
#                                        -h <hue>           ()
#                                        -s <saturation>    (0-254)
#                                        -b <brightness>    (0-254)
#
# examples ...........:
#
#  ./HUE_set_light.py -l KitchenPlant -S on -b 254
#  ./HUE_set_light.py -l Plantpot -S on -h 46014 -s 254 -b 254
#  ./HUE_set_light.py -l Plantpot -S off
#  ./HUE_set_light.py -l Plantpot -S query
#  ./HUE_set_light.py -l query
#
# special ............: 
#
# history ............: 2020.05.02 mg version 0.1
#                       base version
#
### Libraries #################################################################
#
import sys
import getopt
import io
import hashlib
import base64
import os
#
from datetime  import datetime
from time      import sleep, gmtime, strftime
#from threading import Thread
#from uuid      import UUID
#
from phue import Bridge
#
#
### Functions #################################################################
#
# sub : HUE_set_light
#
def HUE_set_light(parameters):
#
# init :
#
    ip_of_hue_bridge = "192.168.2.115"		# IP Address of the Hue Bridge
    b = Bridge(ip_of_hue_bridge)			# Create Bridge Object
#
# Get a dictionary with the light name as the key
#
    light_names = b.get_light_objects('name')
#
# get : parameters
#
    PlightName, Pswitch, Phue, Psaturation, Pbrightness = get_parameters(parameters)
#
#   
    if PlightName == "query" :
       counter = 0
       for light_name in light_names:
           counter += 1
           print (str(counter) + " " + light_name)
       exit (0)

    if Pswitch == "off" :
       light_names[PlightName].on = False
       exit (0)

    if Pswitch == "query" :
       print ("reachable .: " + str(light_names[PlightName].reachable))
       print ("switched on: " + str(light_names[PlightName].on))
       try:
           print ("hue .......: " + str(light_names[PlightName].hue))
       except:
           pass
       try:
           print ("saturation : " + str(light_names[PlightName].saturation))
       except:
           pass
       try:
           print ("brightness : " + str(light_names[PlightName].brightness))
       except:
           pass
       exit (0)

    if Pswitch == "on" :
       light_names[PlightName].on = True

    if Phue != "" :
       phue = int(Phue)
       light_names[PlightName].hue = phue

    if Psaturation != "" :
       psaturation = int(Psaturation)
       light_names[PlightName].saturation = psaturation

    if Pbrightness != "" :
       pbrightness = int(Pbrightness)
       #
       if pbrightness > 254 :
          pbrightness = 254
       #
       if pbrightness < 0 :
          pbrightness = 0
	   #	
       light_names[PlightName].brightness = pbrightness
#
    return ()
#
#------------------------------------------------------------------------------ 
#
# sub : HUE_set_light
#
def HUE_list_lights(parameters):
#
#
    return ()
#
#------------------------------------------------------------------------------ 
#
# sub : get parameters
#
def get_parameters(argv):
#
# init :
#
    PlightName   	= ""
    Pswitch			= ""
    Phue		 	= ""
    Psaturation  	= ""
    Pbrightness		= ""
#
# 
    USAGE = "Usage: " + __file__ + "-l [<lightName>,query] -S [on,off,query] -h <hue> -s <saturation> -b <brightness 0-254>"
#
    try:
        opts, args = getopt.getopt(argv,"?l:S:h:s:b:",["help","lightName=","Switch=","hue=","saturation=","brightness="])
    except getopt.GetoptError:
        print (USAGE)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-?", "--help"):
            print (USAGE)
            sys.exit()
        elif opt in ("-l", "--lightName"):
            PlightName = arg
        elif opt in ("-S", "--switch"):
            Pswitch = arg
        elif opt in ("-h", "--hue"):
            Phue = arg
        elif opt in ("-s", "--saturation"):
            Psaturation = arg
        elif opt in ("-b", "--brightness"):
            Pbrightness = arg
        else:
            print (USAGE)
            sys.exit(2)
#
#   test : parameters
#
    if PlightName == '':						# lightName must contain a value
       print ('parameter -l <lightName> is missing.')
       sys.exit(2)

    #if Pswitch == '':							# switch must contain a value
    #   print ('parameter -S <switch is missing. switch can be on or off')
    #   sys.exit(2)
		
    #Pswitch = Pswitch.lower()
    #if Pswitch != 'on' and Pswitch != 'off' and Pswitch != 'query' :	# switch must be on or off or query
    #   print ('parameter -S <switch must be on or off')
    #   sys.exit(2)
		
    return PlightName, Pswitch, Phue, Psaturation, Pbrightness
#
#------------------------------------------------------------------------------ 
### Main Program ##############################################################
#
if __name__ == '__main__':
#
# get : parameters
#
    parameters  = sys.argv[1:]
    #print "sys.argv : " + str(sys.argv[1:]) + "\n"
    #print "parameter: " + str(parameters) + "\n"
    HUE_set_light(parameters) 
#
### END #######################################################################
