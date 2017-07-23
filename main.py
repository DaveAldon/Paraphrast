# David Crawford - Paraphrast

import subprocess
import socket
import os
import master_dict

def Start():
    header = Awake()

    while True:
        try:
            cmd = input("%s " % header)
            cmd = Paraphrase(cmd)
            proc = subprocess.Popen(cmd, shell=False)
            proc.wait()
        except Exception as e:
            print(e)
            pass

def Paraphrase(cmd):
    for command, translated_command in master_dict.primary.items():
        if command == cmd:
            return translated_command

def Awake():
    if (os.name == "posix"):
        master_dict.flip()
    return "%s:~ %s$" % (socket.gethostname()[:-6], os.getlogin())

Start()
