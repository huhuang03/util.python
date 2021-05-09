import os
from .idea_base import IdeaBase
from ..app import App
from ..env_home_win import *


class IdeaAndroid(IdeaBase):
    def run(self, root):
        App(os.path.join(ANDROID_HOME, "bin", "studio64.exe"), "/Applications/Android Studio.app").start()


def main():
    IdeaAndroid().run('')


if __name__ == '__main__':
    main()
