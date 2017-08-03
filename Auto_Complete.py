from __future__ import unicode_literals
from __future__ import print_function
from prompt_toolkit.contrib.completers.filesystem import PathCompleter
from prompt_toolkit.shortcuts import get_input

def main():
    completer = PathCompleter(only_directories=False, expanduser=True)
    while True:
        try:
            text = get_input('path> ', completer=completer)
        except EOFError:
            break
        except KeyboardInterrupt:
            break
        if text and text.strip():
            print('You selected: ', text)
            break
main()
