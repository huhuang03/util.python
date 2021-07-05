import subprocess

_reserve_branch = ["*", "dev", "main", "master"]


def main():
    output = subprocess.check_output(['git', 'branch', '--merged']).decode('utf-8')
    for name in output.split("\n"):
        name = name.strip()
        if name and len([b for b in _reserve_branch if b in name]) == 0:
            print(f'delete branch {name}')
            subprocess.check_output(['git', 'branch', '-d', name])


if __name__ == '__main__':
    main()
