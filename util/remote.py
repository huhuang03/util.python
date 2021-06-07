import argparse
import os
import subprocess


def login():
    pass


def list_remotes():
    pass


RESERVE_NAME = []


def add(args):
    name = args.name
    if name in RESERVE_NAME:
        exit(f"{name} is reserved, please use another name")
    # ok, let's do some check
    local_ssh_pub = os.path.expanduser("~/.ssh/id_rsa.pub")
    if not os.path.exists(local_ssh_pub):
        exit("Can't find id_rsa.pub file, did you create one?")
    with open(local_ssh_pub, 'r') as f:
        id_rsa_text = f.read().strip()

    assert(id_rsa_text)

    # ok, now let's read the rmote known_keys
    username_host = input("please input username@host: ")
    print(f"ssh {username_host} 'cat .ssh/authorized_keys'")
    subprocess.call(f'ssh {username_host} "cat .ssh/authorized_keys"', shell=True)
    # os.system(f"ssh {username_host} 'cat .ssh/authorized_keys'", =True)

    # os.system('')
    # # how to judge already exit?
    # # we need user input the pwd, and remember the pwd to check exists, and copy??
    # # but I don't want the pwd. for now
    # # so can we check can login for already exists??
    # os.system(f"scp ~/.ssh/id_rsa.pub | ssh {username_host} 'cat >> .ssh/authorized_keys'")


def copy():
    pass


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")
    command_add = subparsers.add_parser("add", help="add a server")
    command_add.add_argument("name", type=str, help="a remember name, not the remote username")
    args = parser.parse_args()
    if args.command == "add":
        add(args)


if __name__ == "__main__":
    pass
