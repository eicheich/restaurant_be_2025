from main import app
import os
import sys

# Gunakan username cPanel Anda dan jalur yang sesuai
# Contoh: "/home/houselab/virtualenv/restaurant_be_2025/3.10/bin/python"
INTERP = os.path.expanduser("/home/houselab/virtualenv/restaurant_be_2025/3.10/bin/python")
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

# FastAPI akan di-serve melalui variabel 'application'
application = app
