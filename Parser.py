# David Crawford - Paraphrast

import master_dict
import os
import subprocess
import socket
import shlex
from prompt_toolkit.shortcuts import get_input

completer = None
windows_supressor = "2>nul"
env = 2
cwd = ""
header = ""
slash = "\\"
output_cmd = []

def Parse():
    cmd = ""
    try:
        cmd = get_input(header, completer=completer)
    except EOFError:
        return
    except KeyboardInterrupt:
        exit()
    except Exception as e:
        print("%s%s" % (header, e))

    global slash, output_cmd
    output_cmd[:] = []

    # Format header of each line. Repeats if nothing was entered
    # TODO Change header based on current directory
    while not cmd:
        cmd = input(header)

    # Seperate our user input into a list for easy calculations
    # Needs try/catch because we don't want to crash if missing end quotes
    try:
        cmd = shlex.split(cmd)
    except Exception as e:
        print("%s%s" % (header, e))
        return

    # Checks if it's a one word statement and simply runs off of primary if so. Saves some time
    if len(cmd) < 2:
        # TODO calculate one line special cases in a seperate location
        if cmd[0] == "cd..":
            MoveUpCd()
            return
        for command, translated_command in master_dict.primary.items():
            if command == cmd[0]:
                # TODO Make OS check happen once and trigger everything automatically
                if env == 2:
                    RunCommand("%s %s" % (translated_command, windows_supressor))
                else:
                    RunCommand(translated_command)
                return

    # Otherwise we're going so start doing the more complicated work...
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
                # If it's not a valid parameter, it might be a special command
                elif Special(cmd[0], param) == 0:
                    return
                else:
                    output_cmd.append(param)

            # Adds the supress error message argument
            if env == 2:
                output_cmd.append(windows_supressor)
            RunCommand(output_cmd)
            return
    print("%s%s" % (header, "command not found"))

def Special(prim, sec):
    for v, k in master_dict.special.items():
        if prim == v:
            try:
                # Dynamically call the function indicated in our special dictionary
                globals()[k](sec)
                return 0
            except Exception as e:
                return 1

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

# After everything has been properly assembled, we run it
def RunCommand(cmd):
    try:
        # TODO Find working way to use shell=False on windows
        proc = subprocess.Popen(cmd, shell=True) if env == 2 else subprocess.Popen(cmd, shell=False)
        proc.wait()
    except Exception as e:
        print(e)

# TODO Get cd dynamic auto complete working
def AutoCompleteCd(path):
    s = subprocess.Popen(["ls", path], shell=True, stdout=subprocess.PIPE).stdout
    service_state = s.read().splitlines()
    temp_li = []
    li = []
    for i in service_state:
        temp_li.append(i.decode('ascii'))
    for i in temp_li[7:-2]:
        li.append(i.split()[4])

def Bind(cmds):
    Auto_Complete.Bind(cmds)

# One time basic OS and user information checks to simulate the Unix terminal experience
def Awake():
    global env, cwd, header, slash, completer
    if (os.name == "posix"):
        # Swaps the primary values
        master_dict.primary = {v: k for k, v in master_dict.primary.items()}
        env = 1
        slash = "/"
    #This is called after the flip so that the auto completer is accessing the latest dictionary
    from Auto_Complete import SystemCompleter
    completer = SystemCompleter()
    cwd = os.getcwd()
    machine_name = socket.gethostname().split(".")
    header = "%s:~ %s$ " % (machine_name[0], os.getlogin())
