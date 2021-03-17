import sys
import os
from pythonex import *
from .env_home_win import JET_BRAINS_HOME
from .app import App

class AppInfo:
    def __init__(self, order, folder, exe = "") -> None:
        self.order = order
        self.folder = folder
        self.exe = exe
        if not self.exe:
            self.exe = folder

all_app = [AppInfo("pcode", "pycharm"), AppInfo("ccode", "clion"), AppInfo("icode", "intelli", "idea64")]

def _get_app_info(order: str) -> AppInfo:
    for app in all_app:
        if app.order == order:
            return app
    exit('unkonw short name for {}'.format(order))


def _get_folder(part_name: str) -> str:
    for fo in os.listdir(JET_BRAINS_HOME):
        if part_name in fo.lower():
            return fo
    exit('can\'t find folder for order: {}'.format(part_name))

def get_exe_in_win(info: AppInfo) -> str:
    app_folder = _get_folder(info.folder)
    bin_folder = os.path.join(JET_BRAINS_HOME, app_folder, 'bin')

    bin_file = ""
    for fo in os.listdir(bin_folder):
        if fo.endswith('.exe') and info.exe in fo:
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
    app_info = _get_app_info(last_name)
    if sys.is_win():
        App(win_path=get_exe_in_win(app_info)).start()
    elif sys.is_mac():
        app_path = get_exe_in_mac(app_info.folder)
        if not app_path:
            exit("Can't find app!! Did you installed it??")
        App(mac_path=app_path).start()
    else:
        exit('unknow platform')
    

if __name__ == "__name__":
    main()