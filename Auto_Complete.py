try:
  import readline
except ImportError:
  import pyreadline as readline

class Completer(object):
    def __init__(self, options):
        self.options = sorted(options)

    def complete(self, text, state):
        if state == 0:  # on first trigger, build possible matches
            if text:  # cache matches (entries that start with entered text)
                self.matches = [s for s in self.options
                                    if s and s.startswith(text)]
            else:  # no text entered, all matches possible
                self.matches = self.options[:]

        # return match indexed by state
        try:
            return self.matches[state]
        except IndexError:
            return None
            
def Bind(cmds):
    completer = Completer(cmds)
    readline.set_completer(completer.complete)
    readline.parse_and_bind('tab: complete')
