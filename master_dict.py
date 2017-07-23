# David Crawford - Paraphrast

primary = {
    "ls": "dir",
    "clear": "cls",
}

def flip():
    global primary
    primary = {v: k for k, v in primary.items()}
