#!/bin/bash
###!/usr/bin/ksh
###############################################################################
#
# HUE_set_light_from_cron.sh : set light called from crontab
# ----------------------------------------------------------
#
# system .............: linux
# directory ..........: ./
# programm ...........: HUE_set_light_from_cron.sh
# version / release ..: 0.1
# date ...............: 02.05.2020 mg version 0.1
#
# programmer .........: Marcel Gross
# departement ........: IT
#
# application group...: 
#                       
# application ........: mm_HUE
#
# usage ..............: The program is used to call the HUE_set_light.py from
#						crontab. It will set the environment variables before calling
#						the python program.
#
# special ............: This program can be called with the following 
#						parameters: 
#						Usage : ${pgname}  [-l <lightName|query>] 
#										   [-S on|off|query] 
#                                          [-h <hue>] 
#                                          [-s <saturation>] 
#                                          [-b <brightness>] 
#                       
#						Examples:
#			
#						HUE_set_light_from_cron.sh -l Plantpot -S on -h 46014 -s 254 -b 254
#                       HUE_set_light_from_cron.sh -l KitchenPlant -S off  -b 254
#
#                       Example: crontab entries for switching the lights at a certain time:
#
#                       $HOME/PycharmProjects/mm_HUE/HUE_set_light_from_cron.sh -l KitchenPlant -S on -b 256        						
#
#                       #
#                       # switch : Lights for KitchenPlant
#                       #
#                       0 8 * * *  /home/gma507/PycharmProjects/mm_HUE/HUE_set_light_from_cron.sh -l KitchenPlant -S on -b 254
#                       0 23 * * *  /home/gma507/PycharmProjects/mm_HUE/HUE_set_light_from_cron.sh -l KitchenPlant -S off
#                       #
#                       # switch : Lights for Plantport
#                       #
#                       0 20 * * *  /home/gma507/PycharmProjects/mm_HUE/HUE_set_light_from_cron.sh -l Plantpot -S on -h 46014 -s 254 -b 254
#                       0 23 * * *  /home/gma507/PycharmProjects/mm_HUE/HUE_set_light_from_cron.sh -l Plantpot -S off
#                       #
#                       
# history ............: 02.05.2020 08:13 mg
#                       base version
#
################################################################################
#
# define : variables
#
#                                                   GENERAL
#
#                                                   # GLOBAL
	user=`whoami`				    				# User-Name
	pgname=`basename ${0}` 	      	           		# Program Name
	pgmdir=$(dirname $0)			    			# Program Directory
	tmppwd=$PWD				    					# 	 
    cd ${pgmdir}				    				# 
    pgmdir=${PWD}                               	# 
    cd ${tmppwd}                                	#
    pgmbas=$(dirname ${pgmdir})                 	# Program Base Directory
#
#                                                   # APPLICATION
#
    applid=""                                   	# Application ID
#
	tmpdir="/tmp"			 				        # Tmp-Directory
	logdir="/tmp/log"			    				# Log-Directory
#
#                                                   # PROGRAM
#
	wrkdir="${pgmdir}"	                    		# Working Directory
	cd ${wrkdir}
#
	inifil="${wrkdir}/${pgname}.ini"	    		# Name of Initialisation-File
    setenv="${wrkdir}/setapplenv.sh"            	# Set Application Environment
	loglhm="${wrkdir}/lhm0101.sh"               	# Log handling functions module
	wrklog="${logdir}/$pgname.log"		    		# Log-File  (PGM.log)
	errlog="${logdir}/$pgname.err"              	# Error-Log (PGM.err)
	uovver=`uname -v`			    				# Unix Operating System Version
    sysnam=`uname -n`			    				# System Name
    pgpanu="$#"				    					# Parameter Number
    pgparm="$*"                                 	# Parameter String
    statyp=""                                   	# Status-Type for Log and Errors
	status=""				    					# Status-Number of Programm
	statxt=""				    					# Status-Text for Log and Errors
#
#                                                   WORK
#
#
#                                                   PARAMETER
#
	PlightName=""				    # Parameter Light Name
	Pswitch=""				    	# Parameter switch 	   (on, off, query)
	Phue=""				    		# Parameter hue        (
	Psaturation=""				    # Parameter saturation (0 - 254)
	Pbrightness=""				    # Parameter brightness (0 - 254)
#
    USAGE="Usage : ${pgname} [-l <lightName|query>] [-S on|off|query] [-h <hue>] [-s <saturation>] [-b <brightness>] "
#
	while getopts :l:S:h:s:b: opt
	do
           case $opt in
                 l)      PlightName=$OPTARG;;
                 S)      Pswitch=$OPTARG;;
                 h)      Phue=$OPTARG;;
                 s)      Psaturation=$OPTARG;;
                 b)      Pbrightness=$OPTARG;;
                 \?)     echo $USAGE
                         exit 2;;
           esac
	done
#
# set : user environment 
#
	cd $HOME
	. ./.profile
#
# set : application environment variables 
#
# 	if [ ! -f ${setenv} ]
#	   then
#	   status="0001"
#           statyp="FAT-I"
#	   statxt="Set Application Environment module ${setenv} file is not existing."
#	   ltsdat=`date +%Y.%m.%d`			# Log Time Stamp Date
#	   ltstim=`date +%H:%M:%S`			# Log Time Stamp Time
##          echo  "${ltsdat} ${ltstim} : \n\n PGM: $0 : ${status} : ${statxt}" >> ${wrklog}
#	   echo -e "${ltsdat} ${ltstim}:${statyp}:$0: ${status} : ${statxt} \007" >& 2
#        else
#         . ${setenv}
#	fi
#
###############################################################################
#
# DEFINE : FUNCTIONS
#
#------------------------------------------------------------------------------
#
# define : Main Function 
#          HUE_set_light_from_cron()
#
HUE_set_light_from_cron()
{
#
# test : input parameters
#
#	test_input_parameters
#
# process : date input format
#
	#echo ${pgparm}
#
# write : output date
#
    cd "$HOME/PycharmProjects/mm_HUE"
	nohup ./HUE_set_light.py ${pgparm} > test_hue_02.log 2>&1 &
}
#
###############################################################################
#
# MAIN PROCEDURE
#
	HUE_set_light_from_cron
#
###############################################################################


