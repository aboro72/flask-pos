import sys
import os
import subprocess
import time
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication
# use the QtWebEngineWidgets
from PyQt5.QtWebEngineWidgets import *


if sys.platform.startswith('Linux'):
    subprocess.Popen(['bash', 'flaskpos_dev.sh'])
else:
    subprocess.Popen(['cmd', 'flaskpos_dev.bat'])

time.sleep(8)


# start my_app
my_app = QApplication(sys.argv)
# open webpage
my_web = QWebEngineView()
my_web.load(QUrl("http://localhost:8000"))
my_web.show()
# sys exit function
sys.exit(my_app.exec_())
