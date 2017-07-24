# David Crawford - Paraphrast

primary = {
    "ls": "dir",
    "clear": "cls",
}

secondary = {
    "ls": ["-a", "FILEPATH"],
    "dir": ["/ah", "FILEPATH"]
}

# Our OS check invokes this function which swaps the primary values
def flip():
    global primary
    primary = {v: k for k, v in primary.items()}
