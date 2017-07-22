# David Crawford - Paraphrast

import subprocess

def Start():
    while True:
        try:
            cmd = input("Type a command: ")

            proc = subprocess.Popen(cmd, shell=False)
            proc.wait()
        except Exception as e:
            print(e)
            pass

Start()
