# David Crawford - Paraphrast

import subprocess
import socket
import os
import Parser
import master_dict

def Start():
    header = Awake()
    
    while True:
        Parser.Parse()

# One time basic OS and user information checks to simulate the UNIX terminal experience
def Awake():
    if (os.name == "posix"):
        master_dict.flip()
        master_dict.environment = "unix"
    master_dict.cwd = os.getcwd()
    master_dict.header = "%s:~ %s$" % (socket.gethostname()[:-6], os.getlogin())

Start()
