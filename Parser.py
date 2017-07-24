# David Crawford - Paraphrast

import master_dict
import os

def Parse(cmd):
    # Checks if it's a one word statement and simply runs off of primary if so
    if " " not in cmd:
        for command, translated_command in master_dict.primary.items():
            if command == cmd:
                return translated_command

    # Otherwise we're going so start doing the more complicated calculations
    output_cmd = []
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
                elif master_dict.environment == "windows":
                    param = param.replace("\\", "/")
                    if cmd[0] == "cd":
                        ChangeDirectory(param)
                    output_cmd.append(param)
                else:
                    param = param.replace("/", "\\")
                    output_cmd.append(param)
            break
    return output_cmd

def ChangeDirectory(dir):
    try:
        os.chdir(dir)
    except Exception as e:
        print(e)
        pass
