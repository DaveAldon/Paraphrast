import subprocess

cmd = input("Directory: ")

s = subprocess.Popen(["dir"], shell=True, stdout=subprocess.PIPE).stdout
service_state = s.read().splitlines()

temp_li = []
li = []

for i in service_state:
    temp_li.append(i.decode('ascii'))

for i in temp_li[7:-2]:
    li.append(i.split()[4])

for i in li:
    if i.startswith(cmd):
        #print(i)
        break

import sys

to = 1000
digits = len(str(to - 1))
delete = "\b" * (digits)
for i in range(to):
    #if i.startswith(cmd):
    print("{0}{1:{2}}".format(delete, i, digits), end="")
    sys.stdout.flush()

#print(li)
