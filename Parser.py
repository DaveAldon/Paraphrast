# David Crawford - Paraphrast

import master_dict

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
            # If our modifier is in the modifier list, then we want the corresponding modifier from its translation
            if cmd[1] in command_keys:
                index = command_keys.index(cmd[1])
                val = master_dict.secondary.get(output_cmd[0])
                output_cmd.append(val[index])

    return output_cmd
