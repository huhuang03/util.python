from setuptools import setup

def create_console_script(*names):
    rst = []
    for name in names:
        rst.append(f'{name} = util.{name}:main')
    return rst

def _get_scripts():
    rst = create_console_script("gitup", "gettopactivity", "ip", "acode", "cmake_ex", "ccode", "unmerged_rm", "lg")
    rst.append('jump = util.jump_and_unjump:jump')
    rst.append('unjump = util.jump_and_unjump:unjump')
    return rst

setup(
    name = 'python shell util',
    version = '1.0.0',
    description = 'shell 简单工具',
    entry_points = {
        'console_scripts': _get_scripts()
    }
)
