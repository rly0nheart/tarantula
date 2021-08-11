#!/usr/bin/env python3
import sys
import colorama
from colorama import Back as bg

colors = True
machine = sys.platform # Detecting the os of current system
if machine.lower().startswith(('os', 'win', 'darwin', 'ios')):
    colors = False # Colors will not be displayed in mac & windows
if not colors:
    RESET = GREEN = GRAY = YELLOW = RED = ""
else:
    colorama.init()
    WHITE = colorama.Fore.WHITE
    GRAY = colorama.Fore.LIGHTBLACK_EX
    RESET = colorama.Fore.RESET
    YELLOW = colorama.Fore.YELLOW
    RED = colorama.Fore.RED
