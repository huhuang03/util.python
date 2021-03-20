import os
import sys

# Find program in windows
# It will search program in X:\Program Files X:\Program Files(x86)

def _find_in_folder(folder_name, to_find):
    to_find_low = to_find.lower()
    if os.path.exists(folder_name) and os.path.isdir(folder_name):
        for f in os.listdir(folder_name):
            if to_find_low in f.lower():
                print(os.path.join(folder_name, f))

def _find(disk_name, to_find):
    path = os.path.join(f"{disk_name}:", 'Program Files')
    _find_in_folder(path, to_find)
    path = os.path.join(f"{disk_name}:", 'Program Files (x86)')
    _find_in_folder(path, to_find)


def main():
    if not os.name == 'nt':
        exit('only work on window')
    if len(sys.argv) < 2:
        exit(f"usage: {sys.argv[0]} to_find")
    for i in range(ord('A'), ord('Z')):
        _find(str(chr(i)), sys.argv[1])

if __name__ == '__main__':
    main()