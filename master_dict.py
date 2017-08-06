# David Crawford - Paraphrast

primary = {
    "ls": "dir",
    "clear": "cls",
    "cd": "cd",
    "ping": "ping",
    "ps": "tasklist",
    "cat": "type",
    "vm_stat": "mem",
    # TODO vm_stat is for macs, but "free" is the linux variant. Both should
    # map to "mem" but mem should map to the appropriate OS
}

secondary = {
    "ls": ["-a", "FILEPATH"],
    "dir": ["/a", "FILEPATH"],
    "cd": ["FILEPATH"],
    "ping": ["ADDRESS"],
}

special = {
    "cd": "RunCd",
}
