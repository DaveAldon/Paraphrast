# David Crawford - Paraphrast

import master_dict
import os
import subprocess

def Parse():
    # Format header of each line
    # TODO Change header based on current directory
    cmd = input("%s " % master_dict.header)

    # Checks if it's a one word statement and simply runs off of primary if so
    if " " not in cmd:
        # TODO Put special cases in one spot
        if cmd == "cd..":
            MoveUpCd("/")
            return
        for command, translated_command in master_dict.primary.items():
            if command == cmd:
                # TODO Make OS check happen once and trigger everything automatically
                if master_dict.environment == "windows":
                    RunCommand(translated_command + " %s" % master_dict.windows_supressor)
                else:
                    RunCommand(translated_command)
                return

    # Otherwise we're going so start doing the more complicated work
    output_cmd = []
    # Seperate our user input into a list for easy calculations
    cmd = cmd.split()

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
                elif cmd[0] == "cd":
                    RunCd(param)
                    return
            # Adds the supress error message argument
            if master_dict.environment == "windows":
                output_cmd.append(master_dict.windows_supressor)
            RunCommand(output_cmd)
            return
    print("Command Not Found")

def RunCd(path):
    slash = "/"
    if master_dict.environment == "windows":
        slash = "\\"
    if path not in "..":
        MoveDownCd(path, slash)
    else:
        MoveUpCd(slash)

def MoveDownCd(path, slash):
    path_temp = master_dict.cwd + slash + path
    master_dict.cwd = path_temp
    os.chdir(master_dict.cwd)

def MoveUpCd(slash):
    path_temp = master_dict.cwd.split(slash)
    path_temp.pop()
    master_dict.cwd = slash.join(path_temp)
    os.chdir(master_dict.cwd)

def RunCommand(cmd):
    try:
        # Run the command
        # TODO Find working way to use shell=False on windows
        if master_dict.environment == "windows":
            proc = subprocess.Popen(cmd, shell=True)
        else:
            proc = subprocess.Popen(cmd, shell=False)
        proc.wait()
    except Exception as e:
        print(e)
        pass
