# David Crawford - Paraphrast

import master_dict
import os
import subprocess
import socket

windows_supressor = "2>nul"
env = 2
cwd = ""
header = ""
slash = "\\"

def Parse():
    global slash
    # Format header of each line
    # TODO Change header based on current directory
    cmd = input("%s " % header)
    # Seperate our user input into a list for easy calculations
    cmd = cmd.split()

    # Checks if it's a one word statement and simply runs off of primary if so. Saves some time
    if len(cmd) < 2:
        # TODO calculate special cases in a seperate location
        if cmd[0] == "cd..":
            MoveUpCd(slash)
            return
        for command, translated_command in master_dict.primary.items():
            if command == cmd[0]:
                # TODO Make OS check happen once and trigger everything automatically
                if env == 2:
                    RunCommand("%s %s" % (translated_command, windows_supressor))
                else:
                    RunCommand(translated_command)
                return

    # Otherwise we're going so start doing the more complicated work
    output_cmd = []
    # Searches for the main command
    for command, command_keys in master_dict.secondary.items():
        if command == cmd[0]:
            # Output the translated primary
            output_cmd.append(master_dict.primary.get(command))
            # Now we begin working through the parameters
            for param in cmd[1:]:
                # If our modifier is in the modifier list, then we want the corresponding modifier from its translation
                if param in command_keys:
                    index = command_keys.index(param)
                    val = master_dict.secondary.get(output_cmd[0])
                    output_cmd.append(val[index])
                # If it's not a valid parameter, it might be a path
                # TODO calculate special cases in a seperate location
                elif cmd[0] == "cd":
                    RunCd(param)
                    return
                elif cmd[0] == "ping":
                    output_cmd.append(param)
            # Adds the supress error message argument
            if env == 2:
                output_cmd.append(windows_supressor)
            RunCommand(output_cmd)
            return
    print("Command Not Found")

def RunCd(path):
    global slash
    # TODO continue to test that this is working properly
    if path not in "..":
        MoveDownCd(path)
    else:
        MoveUpCd()

def MoveDownCd(path):
    global cwd, slash
    cwd = cwd + slash + path
    os.chdir(cwd)

def MoveUpCd():
    global cwd, slash
    path_temp = cwd.split(slash)
    path_temp.pop()
    cwd = slash.join(path_temp)
    os.chdir(cwd)

def RunCommand(cmd):
    try:
        # Run the command
        # TODO Find working way to use shell=False on windows
        proc = subprocess.Popen(cmd, shell=True) if env == 2 else subprocess.Popen(cmd, shell=False)
        proc.wait()
    except Exception as e:
        print(e)

# One time basic OS and user information checks to simulate the UNIX terminal experience
def Awake():
    global env, cwd, header, slash
    if (os.name == "posix"):
        master_dict.flip()
        env = 1
        slash = "/"
    cwd = os.getcwd()
    header = "%s:~ %s$" % (socket.gethostname()[:-6], os.getlogin())
