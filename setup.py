from setuptools import setup

def create_console_script(*names):
    rst = []
    for name in names:
        rst.append(f'{name} = util.{name}:main')
    return rst

def _create_jebran_command(name):
    return '{} = util.jet_brains:main'.format(name)

def _get_scripts():
    # why I need creat this by hand??
    rst = create_console_script("gitup", "gettopactivity", "ip", "acode", "cmake_ex", "unmerged_rm",\
         "lg", 'utf8_2_utf8bom', "save_space", 'find_program', 'rn_ex', 'json2bean', 'jt_ex')
    rst.append(_create_jebran_command('pcode'))
    rst.append(_create_jebran_command('ccode'))
    rst.append(_create_jebran_command('icode'))
    rst.append(_create_jebran_command('hcode'))
    rst.append(_create_jebran_command('wcode'))
    return rst

setup(
    name = 'python shell util',
    version = '1.0.0',
    description = 'shell 简单工具',
    entry_points = {
        'console_scripts': _get_scripts()
    }
)
