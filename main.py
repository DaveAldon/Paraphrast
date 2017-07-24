# David Crawford - Paraphrast

import subprocess
import socket
import os
import Parser
import master_dict

def Start():
    header = Awake()

    while True:
        try:
            # Format header of each line
            cmd = input("%s " % header)
            cmd = Paraphrase(cmd)
            # Run the command
            # TODO Find working way to use shell=False on windows
            proc = subprocess.Popen(cmd, shell=True)
            proc.wait()
        except Exception as e:
            print(e)
            pass

# Invokes the parsing module
def Paraphrase(cmd):
    return Parser.Parse(cmd)

# One time basic OS and user information checks to simulate the UNIX terminal experience
def Awake():
    if (os.name == "posix"):
        master_dict.flip()
    return "%s:~ %s$" % (socket.gethostname()[:-6], os.getlogin())

Start()
