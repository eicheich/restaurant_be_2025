from main import app
import os
import sys

INTERP = os.path.expanduser("/home/YOUR_CPANEL_USERNAME/virtualenv/YOUR_PROJECT_PATH/3.10/bin/python")
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

application = app
