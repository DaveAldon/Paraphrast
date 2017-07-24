# David Crawford - Paraphrast

primary = {
    "ls": "dir",
    "clear": "cls",
    "cd": "cd",
    "cd..": "cd.."
}

secondary = {
    "ls": ["-a", "FILEPATH"],
    "dir": ["/a", "FILEPATH"],
    "cd": ["FILEPATH"],
}

environment = "windows"

# Our OS check invokes this function which swaps the primary values
def flip():
    global primary
    primary = {v: k for k, v in primary.items()}
