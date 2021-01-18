import os

def jump():
    os.system('export HTTP_PROXY="http://127.0.0.1:1080"')
    os.system('export HTTPS_PROXY="https://127.0.0.1:1080"')

def unjump():
    os.system('unset HTTP_PROXY')
    os.system('unset HTTPS_PROXY')