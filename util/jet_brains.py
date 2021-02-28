import sys
import os
from pythonex import *
from .env_home_win import JET_BRAINS_HOME
from .app import App

def _get_app_shortname(order: str):
    if order == "pcode":
        return "pycharm"
    elif order == 'ccode':
        return 'clion'
    else:
        exit('unkonw short name for {}'.format(order))


def _get_folder(part_name: str) -> str:
    for fo in os.listdir(JET_BRAINS_HOME):
        if part_name in fo.lower():
            return fo
    exit('can\'t find folder for order: {}'.format(part_name))

def get_exe_in_win(part_name: str) -> str:
    app_folder = _get_folder(part_name)
    bin_folder = os.path.join(JET_BRAINS_HOME, app_folder, 'bin')

    bin_file = ""
    for fo in os.listdir(bin_folder):
        if fo.endswith('.exe') and part_name in fo:
            bin_file = fo
    bin_path = os.path.join(bin_folder, bin_file)
    return bin_path

def get_exe_in_mac(order_name: str) -> str:
    folder = "/Applications"
    for f in os.listdir(folder):
        if order_name in f.lower() and f.endswith(".app"):
            return os.path.join(folder, f)
    return ""


def main():
    last_name = os.path.basename(sys.argv[0])
    app_short_name = _get_app_shortname(last_name)
    if sys.is_win():
        App(win_path=get_exe_in_win(app_short_name)).start()
    elif sys.is_mac():
        App(mac_path=get_exe_in_mac(app_short_name)).start()
    else:
        exit('unknow platform')
    

if __name__ == "__name__":
    main()