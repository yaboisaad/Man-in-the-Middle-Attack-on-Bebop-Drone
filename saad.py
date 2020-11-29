#!/usr/bin/env python
import sys
import os
import code
import readline
import rlcompleter
import socket
import tkinter as tk
sys.path.append('../src')
from Bybop_Discovery import *
import Bybop_Device

print('Saad, Amir, and Hebah are looking for available drones....')
discovery = Discovery([DeviceID.BEBOP_DRONE, DeviceID.JUMPING_SUMO])
discovery.wait_for_change()
devices = discovery.get_devices()
discovery.stop()
if not devices:
    print('Oops ...')
    sys.exit(1)
device = next(iter(devices.values()))

print('Found a drone, about to connect to  :::::  ' + get_name(device))
d2c_port = 54321
controller_type = "PC"
controller_name = "bybop shell"

drone = Bybop_Device.create_and_connect(device, d2c_port, controller_type, controller_name)
if drone is None:
    print('Coudlnt connect to a drone try again..')
    sys.exit(1)

drone.dump_state()
vars = globals().copy()
vars.update(locals())
readline.set_completer(rlcompleter.Completer(vars).complete)
readline.parse_and_bind("tab: complete")
shell = code.InteractiveConsole(vars)

def onKeyPress(event):
    if event.char == "t":
        text.insert('end', 'Taking off\n')
        drone.take_off()
    elif event.char == "l":
        text.insert('end', 'Landing\n')
        drone.land()
    elif event.char == "w":
        text.insert('end', 'Set pitch to 50\n')
        drone.send_data('ARDrone3','Piloting','PCMD',True,0,75,0,0,0)
    elif event.char == "s":
        text.insert('end', 'Set pitch to -50\n')
        drone.send_data('ARDrone3','Piloting','PCMD',True,0,-75,0,0,0)
    elif event.char == "a":
        text.insert('end', 'Set roll to -50\n')
        drone.send_data('ARDrone3','Piloting','PCMD',True,-75,0,0,0,0)
    elif event.char == "d":
        text.insert('end', 'Set roll to 50\n')
        drone.send_data('ARDrone3','Piloting','PCMD',True,75,0,0,0,0)
    elif event.char == "u":                                           
        text.insert('end', 'Set gaz to 50\n')
        drone.send_data('ARDrone3','Piloting','PCMD',True,0,0,0,75,0) # Press U to move up
    elif event.char == "j":                                           # Press J to move down
        text.insert('end', 'Set gaz to -50\n')
        drone.send_data('ARDrone3','Piloting','PCMD',True,0,0,0,-75,0)
    elif event.char == " ":
        text.insert('end', 'Set all to 0\n')
        drone.send_data('ARDrone3','Piloting','PCMD',True,0,0,0,0,0)
    else:
        text.insert('end', 'Invalid Key: %s\n' % (event.char, ))
    text.see(tk.END)

root = tk.Tk()
root.geometry('300x200')
text = tk.Text(root, background='black', foreground='white', font=('Comic Sans MS', 14))
text.pack()
root.bind('<KeyPress>', onKeyPress)
root.mainloop()
drone.stop()
