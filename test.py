from __future__ import unicode_literals

from prompt_toolkit.contrib.completers import WordCompleter
from prompt_toolkit import prompt

import msvcrt
import sys


animal_completer = WordCompleter([
    'alligator',], ignore_case=True)

ch = ""
from msvcrt import getch

while True:
    #msvcrt.getch()
    c = msvcrt.getwche()

    if ord(c) == 13:
        print("Enter key pressed")

    if ord(c) == 8:
        sys.stdout.write(' \010')
        sys.stdout.flush()
        ch = ch[:-1]
        #print("Delete key pressed")

    if ord(c) == 9: #tab key
        sys.stdout.write('\033[2K\033[1G')
        sys.stdout.flush()
        text = prompt(ch, completer=animal_completer,
                      complete_while_typing=True)

    if ord(c) == 27: #ESC
        break

    else:
        ch += c
print(ch)







def main():
    text = prompt('Give some animals: ', completer=animal_completer,
                  complete_while_typing=True)
    print('You said: %s' % text)
