from __future__ import unicode_literals
from __future__ import print_function
from prompt_toolkit.contrib.completers.filesystem import PathCompleter
from prompt_toolkit.shortcuts import get_input
from prompt_toolkit.contrib.regular_languages.completion import GrammarCompleter
from prompt_toolkit.contrib.regular_languages.compiler import compile
from prompt_toolkit.contrib.completers.filesystem import ExecutableCompleter
from prompt_toolkit.contrib.completers import WordCompleter
import master_dict

__all__ = (
    'SystemCompleter',
)

class SystemCompleter(GrammarCompleter):
    """
    Completer for system commands.
    """
    def __init__(self):
        # Compile grammar.
        g = compile(
            r"""
                # First we have an executable.
                (?P<executable>[^\s]+)
                # Ignore literals in between.
                (
                    \s+
                    ("[^"]*" | '[^']*' | [^'"]+ )
                )*
                \s+
                # Secondary grammar
                (
                    (?P<filename>[^\s]+) |
                    -(?P<modifier>[^\s]+) |
                    "(?P<double_quoted_filename>[^\s]+)" |
                    '(?P<single_quoted_filename>[^\s]+)'
                )
            """,
            escape_funcs={
                'double_quoted_filename': (lambda string: string.replace('"', '\\"')),
                'single_quoted_filename': (lambda string: string.replace("'", "\\'")),
            },
            unescape_funcs={
                'double_quoted_filename': (lambda string: string.replace('\\"', '"')),  # XXX: not enterily correct.
                'single_quoted_filename': (lambda string: string.replace("\\'", "'")),
            })

        # Create GrammarCompleter
        super(SystemCompleter, self).__init__(
            g,
            {
                'executable': WordCompleter(master_dict.primary, meta_dict=master_dict.primary),
                'modifier': WordCompleter(master_dict.secondary),
                'filename': PathCompleter(only_directories=False, expanduser=True),
                'double_quoted_filename': PathCompleter(only_directories=False, expanduser=True),
                'single_quoted_filename': PathCompleter(only_directories=False, expanduser=True),
            })
