# smart choice idea
# for now first implement check android.
import os
import sys
from .idea_android import IdeaAndroid
from .idea_code import IdeaCode
from .idea_base import IdeaBase
from .idea_pycharm import IdeaPycharm


def main():
    if len(sys.argv) < 2:
        exit('usage: {} directory'.format(sys.argv[0]))

    root = sys.argv[1]
    if not os.path.exists(root):
        exit('for now, I didn\'t think well how to handle directory not exist')

    idea: IdeaBase = IdeaCode()
    if _judge_is_android(root):
        idea = IdeaAndroid()
    elif _judge_is_python(root):
        idea = IdeaPycharm()
    idea.run(root)


def _judge_is_android(root) -> bool:
    return False


def _judge_is_python(root: str) -> bool:
    return "setup.py" in os.listdir(root)


if __name__ == '__main__':
    main()