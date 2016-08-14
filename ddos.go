#!/usr/bin/python2

import hexchat
import random

__module_name__ = "Ddos simulator"
__module_author__ = "KristinaEtc"
__module_version__ = "0.1"
__module_description__ = "Ddos simulator"

world = ['sun','moon','stars','planets','galaxies','oceans','mountains','trees','mom','dad','boss','job',
'dollar','degree''medicine','customers','nobody','light','fan','businessess']

def send_stuff(word, word_eol, userdata):
    allah_msg = "%s are not doing Allah is doing" %(random.choice(world))

    channel = hexchat.get_info("channel")
    if len(word) < 2: #print message to a channel
        hexchat.command("MSG %s %s" %(channel, my_msg))
    elif len(word) == 2: #print private message to a user
        hexchat.command("MSG %s %s" %(word[1], my_msg))
    elif len(word) == 3: #ddos version for boorish children
        for x in range(0, 100):
            hexchat.command("MSG %s %s" %(word[1], my_msg))

hexchat.hook_command("ddos", send_stuff)



