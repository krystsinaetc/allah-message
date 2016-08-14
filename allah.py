#!/usr/bin/python2

import hexchat
import random

__module_name__ = "Allah did it"
__module_author__ = "KristinaEtc"
__module_version__ = "0.1"
__module_description__ = "Allah stuff for user"

world = ['Allah1', 'Allah2', 'Allah3', 'Allah4', 'Allah5', 'Allah6', 'Allah7', 'Allah8', 'Allah9']


def send_allah_stuff(word, word_eol, userdata):
    my_msg = "%s are not doing Allah is doing" %(random.choice(world))
    #channel = hexchat.get_info("")
    channel = hexchat.get_info("channel")
    if len(word) < 2:
        hexchat.command("MSG %s %s" %(channel, my_msg))
    else if :
            hexchat.command("MSG %s %s" %(word[1], my_msg))

hexchat.hook_command("allah", send_allah_stuff)



