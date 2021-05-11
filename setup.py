from setuptools import setup
import os


def create_console_script(*names):
    rst = []
    for name in names:
        rst.append(f'{name} = util.{name}:main')
    return rst


def _create_command(name, file_path):
    return f'{name} = util.{file_path}:main'


def _create_jebrain_command(name):
    return '{} = util.jet_brains:main'.format(name)


def _create_by_cli():
    '''
    Fuck I don't write for now.
    :return:
    '''
    pwd = os.getcwd()
    cli_path = os.path.join(pwd, 'util/cli/')
    if os.path.exists(cli_path):
        for f in os.listdir(cli_path):
            print(f)


COMMANDS = ["gitup", "gettopactivity", "ip", "idea.idea_android", "cmake_ex", "unmerged_rm",
            "lg", 'utf8_2_utf8bom', "save_space", 'find_program', 'rn_ex', 'json2bean', 'jt_code', 'idea.scode']

def _get_scripts():
    # why I need creat this by hand??
    rst = create_console_script(*COMMANDS)
    _create_by_cli()
    rst.append(_create_command('acode', 'idea.idea_android'))
    rst.append(_create_command('scode', 'idea.scode'))
    rst.append(_create_jebrain_command('pcode'))
    rst.append(_create_jebrain_command('ccode'))
    rst.append(_create_jebrain_command('icode'))
    rst.append(_create_jebrain_command('hcode'))
    rst.append(_create_jebrain_command('wcode'))
    return rst


setup(
    name='python shell util',
    version='1.0.0',
    description='shell 简单工具',
    entry_points={
        'console_scripts': _get_scripts()
    }
)
