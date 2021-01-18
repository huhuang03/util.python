import os
import shutil

_dir = os.getcwd()

def _del(path):
    name = os.path.basename(path)
    if os.path.exists(path):
        print("delete " + name)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)

def command_clean():
    FILE_CMAKE_CACHE = "CMakeCache.txt"
    path_cmake_cache = os.path.join(_dir, FILE_CMAKE_CACHE)
    _del(path_cmake_cache)
    _del(os.path.join(_dir, "CMakeFiles"))

def main():
    command_clean()

if __name__ == "__main__":
    command_clean()
