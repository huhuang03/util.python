import sys
from sys import platform
import subprocess
import os
from . import App
from .env_home_win import CLION_HOME

def main():
    App(os.path.join(CLION_HOME, "bin", "clion64.exe"), "/Applications/CLion.app").start()