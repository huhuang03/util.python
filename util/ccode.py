import sys
from sys import platform
import subprocess
import os
from .util import JetBrainsApp
from .env_home_win import CLION_HOME

def main():
    JetBrainsApp(os.path.join(CLION_HOME, "bin", "clion64.exe"), "/Applications/CLion.app").start()