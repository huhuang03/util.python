import subprocess


def main():
    output = subprocess.check_output(['git', 'branch', '--merged']).decode('utf-8')
    for name in output.split("\n"):
        name = name.strip()
        if name and 'dev' not in name and '*' not in name:
            subprocess.check_output(['git', 'branch', '-d', name])


if __name__ == '__main__':
    main()
