import sys
import os
from pythonex import *
import subprocess
from .env_home_win import JET_BRAINS_HOME
from .app import App

def _get_fodler_part_name(order: str):
    if order == "pcode":
        return "pycharm"
    elif order == 'ccode':
        return 'clion'

    else:
        exit('unknow command {}'.format(order))


def _get_folder(order: str) -> str:
    part_name = _get_fodler_part_name(order)
    for fo in os.listdir(JET_BRAINS_HOME):
        if part_name in fo.lower():
            return fo
    exit('can\'t find folder for order: {}'.format(order))


def main():
    order_name = os.path.basename(sys.argv[0])
    part_name = _get_fodler_part_name(order_name)
    app_folder = _get_folder(order_name)
    bin_folder = os.path.join(JET_BRAINS_HOME, app_folder, 'bin')

    bin_file = ""
    for fo in os.listdir(bin_folder):
        if fo.endswith('.exe') and part_name in fo:
            bin_file = fo

    if not bin_file:
        raise('can\'t find bin_file')

    bin_path = os.path.join(bin_folder, bin_file)
    App(bin_path).start()


if __name__ == "__name__":
    main()