import sys
from .util import *
import os
import subprocess
from sys import call_tracing, platform

DETACHED_PROCESS = 8


class App:
    """
    Represent an application
    """

    def __init__(self, win_path='', mac_path=''):
        self.win_path = win_path
        self.mac_path = mac_path

    def start_in_folder(self, folder):
        full_dir_path = os.path.abspath(folder)

        if not os.path.exists(full_dir_path):
            raise Exception("Why path not exist: " + full_dir_path)

        if is_windows():
            if not self.win_path:
                exit('exe file not find')
            if not os.path.exists(self.win_path):
                raise Exception("Why exe not exist: " + self.win_path)
            # Popen is not good because it will still controlled by the process open the win_path
            # how to start the bat??
            try:
                subprocess.Popen([self.win_path, full_dir_path], cwd=full_dir_path, creationflags=DETACHED_PROCESS,
                                 close_fds=True)
            except Exception as e:
                print(f"win_path: {self.win_path}")
                raise e
        elif is_mac():
            if not self.mac_path:
                exit('mac application path not specified')
            subprocess.Popen(['open', '-a', self.mac_path, folder], cwd=full_dir_path)
        else:
            raise Exception(f"Not work on {platform}")

    def start(self):
        if len(sys.argv) >= 2:
            dir_name = sys.argv[1]
        else:
            dir_name = "."
        self.start_in_folder(dir_name)