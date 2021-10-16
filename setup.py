#!/usr/bin/env python3

import argparse
import enum

class ShellType(enum.Enum):
    # NONE = 'none'
    BASH = 'bash'
    ZSH = 'zsh'

    def __str__(self):
        return self.value


# Get command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--shell", dest = "shell", choices=ShellType, type=ShellType, help="Give the shell you want to use")
parser.add_argument("-c", "--configlocation", dest = "configlocation", default="~/configuration", help="Path to your configuration directory")
args = parser.parse_args()

# Constants
pre_decorator = "="*20 + " ADDED FROM CONFIG SCRIPT " + "="*20
post_decorator = "="*66
to_rc_file = '''
# Add custom aliases
source {loc}/aliases/aliases.txt
source {loc}/aliases/git_aliases.txt

alias tmux='tmux -f {loc}/dots/.tmux.conf'
'''

def append_to_file():
    print("Config location: {}".format(args.configlocation))
    full_text = pre_decorator + to_rc_file.format(loc=args.configlocation) + post_decorator

    
    if args.shell == ShellType.BASH:
        file_name = "$HOME/.bashrc"
        append(file_name, full_text)
    elif args.shell == ShellType.ZSH:
        file_name = "$HOME/.zshrc"
        append(file_name, full_text)
    else:
        print("Your shell ({}) not supported yet".format(args.shell))


def append(file_name, text):
    with open(file_name, "a") as file_object:
        file_object.write("\n" + text)

append_to_file()
