import sys

colors = True
machine = sys.platform # Detecting the os of current system
if machine.lower().startswith(('os', 'win', 'darwin', 'ios')):
    colors = False # Colors will not be displayed in mac & windows
if not colors:
    reset = red = white = green = yellow = ''
else:
    white = "\x1b[97m"
    green = "\x1b[92m"
    red = "\x1b[91m"
    yellow = "\x1b[93m"
    reset = "\x1b[0m"
