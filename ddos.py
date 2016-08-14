#!/usr/bin/python2

import hexchat
import random
import getpass

__module_name__ = "Ddos simulator"
__module_author__ = "KristinaEtc"
__module_version__ = "0.1"
__module_description__ = "Ddos simulator"



def send_stuff(word, word_eol, userdata):
    curr_user = getpass.getuser()
    fname = '/home/' + curr_user + '/.config/hexchat/addons/allah.txt'
    with open(fname) as f:
        content = f.readlines()

    channel = hexchat.get_info("channel")
    if len(word) == 2: #ddos version for boorish children
        for x in range(0, 1000):
            msg = random.choice(content)
            hexchat.command("MSG %s %s" %(word[1], msg))

hexchat.hook_command("ddos", send_stuff)



