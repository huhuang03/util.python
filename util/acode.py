import sys
from sys import platform
import subprocess
import os
from .util import JetBrainsApp
from .env_home_win import *

def main():
    JetBrainsApp(os.path.join(ANDROID_HOME, "bin", "studio64.exe"), "/Applications/Android Studio.app").start()