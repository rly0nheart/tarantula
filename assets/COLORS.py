import sys

colors = True
machine = sys.platform # Detecting the os of current system
if machine.lower().startswith(('os', 'win', 'darwin', 'ios')):
    colors = False # Colors will not be displayed in mac & windows
if not colors:
    RESET = RED = WHITE = GREEN = YELLOW = ''
else:
    WHITE = "\x1b[97m"
    GREEN = "\x1b[92m"
    RED = "\x1b[91m"
    RESET = "\x1b[0m"
    YELLOW = "\x1b[93m"
   
