#!/usr/bin/python
import sys
import os
import time
import subprocess
from pushbullet import Pushbullet

server_name = subprocess.check_output("cat pylinuxbot.log |grep command_line | grep ngrok.io | cut -d' ' -f 10 | cut -d= -f 2 | cut -d: -f 2", shell=True)
server_name = server_name.rstrip('\n')

if (server_name != ""):
    pb = Pushbullet("o.tfsE1vln5IaF7p7aUmOwusJZHItPiB3F")
    hw = pb.get_device('Samsung SM-G955F')
    hw.push_note("PPTRemote", "Server name")
    hw.push_note("", server_name)
else:
    print("Error getting server name")
    print("cat pylinuxbot.log")

