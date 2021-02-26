import sys
from sys import platform
import subprocess
import os
from . import App
from .env_home_win import *

def main():
    App(os.path.join(ANDROID_HOME, "bin", "studio64.exe"), "/Applications/Android Studio.app").start()