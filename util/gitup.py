import os


def main():
    os.system('git add .')
    msg = input('Please input commit message: ')
    if not msg:
        msg = 'update'
    os.system('git commit --no-verify -a -m "%s"' % msg)
    os.system('git push')
