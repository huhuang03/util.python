import os
from .idea_base import IdeaBase
from ..app import App
from ..env_home_win import *
import configparser


# how can we load the local.init

def _get_android_home():
    local_ini_path = os.path.join(os.path.dirname(__file__), "../../local.ini")
    folder = ANDROID_HOME
    if os.path.exists(local_ini_path):
        config = configparser.ConfigParser()
        config.read(local_ini_path)
        folder = config['DEFAULT']['AS_HOME']
    return os.path.join(folder, "bin", "studio64.exe")


class IdeaAndroid(IdeaBase):
    def run(self, root):
        App(_get_android_home(), "/Applications/Android Studio.app").start()


def main():
    IdeaAndroid().run('')


if __name__ == '__main__':
    main()
