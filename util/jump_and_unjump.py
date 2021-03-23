import os
from .util import *

def jump():
    if is_windows():
        add_to_clip_board('$Env:http_proxy="http://127.0.0.1:7890";$Env:https_proxy="http://127.0.0.1:7890"')
    else:
        os.system('export HTTP_PROXY="http://127.0.0.1:1080"')
        os.system('export HTTPS_PROXY="https://127.0.0.1:1080"')

def unjump():
    if is_windows():
        exit('unimplement in windows')
    else:
        os.system('unset HTTP_PROXY')
        os.system('unset HTTPS_PROXY')