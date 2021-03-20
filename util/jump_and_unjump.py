import os
from .util import *

def jump():
    if os.name == 'nt':
        # how to output the shell and let user input this shell?
        add_to_clip_board('$Env:http_proxy="http://127.0.0.1:7890";$Env:https_proxy="http://127.0.0.1:7890"')
    else:
        os.system('export HTTP_PROXY="http://127.0.0.1:1080"')
        os.system('export HTTPS_PROXY="https://127.0.0.1:1080"')

def unjump():
    if os.name == 'nt':
        os.system('unset HTTP_PROXY')
        os.system('unset HTTPS_PROXY')
    else:
        pass