import os

def main():
    if os.name == 'nt':
        print('$Env:http_proxy="http://127.0.0.1:7890";$Env:https_proxy="http://127.0.0.1:7890"')
    else:
        print('not work on {}'.format(os.name))


if __name__ == '__main__':
    main()