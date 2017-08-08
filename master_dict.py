# David Crawford - Paraphrast

primary = {
    "ls": "dir",
    "clear": "cls",
    "cd": "cd",
    "ping": "ping",
    "ps": "tasklist",
    "cat": "type",
    "grep": "find",
    "rm": "rmdir",
    "mkdir": "mkdir",
    "vm_stat": "mem",
    "env": "set",
    # TODO vm_stat is for macs, but "free" is the linux variant. Both should
    # map to "mem" but mem should map to the appropriate OS
}

secondary = {
    "ls": ["-a", "FILEPATH"],
    "dir": ["/a", "FILEPATH"],
    "rmdir": ["/s"],
    "rm": ["-r"],
    "cd": ["FILEPATH"],
    "ping": ["ADDRESS"],
    "mkdir": ["FILENAME"],
}

secondary_h = {
    "a":"",
    "r":"",
}

secondary_s = {
    "a":"",
    "s":"",
}

special = {
    "cd": "RunCd",
}
