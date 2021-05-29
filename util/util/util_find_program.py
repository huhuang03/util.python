import os


# Find program in windows
# It will search program in X:\Program Files X:\Program Files(x86)
def _find_in_folder(folder_name, to_find) -> [str]:
    # print("folder_name: " + folder_name)
    rst = []
    to_find_low = to_find.lower()
    if os.path.exists(folder_name) and os.path.isdir(folder_name):
        for f in os.listdir(folder_name):
            # print('f: ' + f)
            if to_find_low in f.lower():
                rst.append(os.path.join(folder_name, f))
    else:
        pass
        # print('not exist: ' + folder_name)
    return rst


def _find(disk_name, to_find):
    rst = []
    path = os.path.join(f"{disk_name}:\\", 'Program Files')
    rst += _find_in_folder(path, to_find)
    path = os.path.join(f"{disk_name}:\\", 'Program Files (x86)')
    rst += _find_in_folder(path, to_find)
    return rst


def find_program(program_part_name) -> [str]:
    # print('program_part_name: ' + program_part_name)
    if not os.name == 'nt':
        exit('only work on window')
    rst = []
    for i in range(ord('A'), ord('Z')):
        rst += _find(str(chr(i)), program_part_name)
    # print('rst: ' + ','.join(rst))
    return rst