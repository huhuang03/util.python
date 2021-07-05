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
    """
    Fuck I don't write for now.
    :return:
    """
    pwd = os.getcwd()
    cli_path = os.path.join(pwd, 'util/cli/')
    if os.path.exists(cli_path):
        for f in os.listdir(cli_path):
            print(f)


COMMANDS = ["gitup", "gettopactivity", "ip", "cmake_ex", "merged_rm", "an_util",
            "lg", 'utf8_2_utf8bom', "save_space", 'find_program', 'rn_ex', 'json2bean', 'jt_code']


def _get_scripts():
    # why I need create this by hand??
    rst = create_console_script(*COMMANDS)
    _create_by_cli()
    rst.append(_create_command('acode', 'idea.idea_android'))
    rst.append(_create_command('scode', 'idea.scode'))
    rst.append(_create_command('pcode', 'idea.idea_pycharm'))
    rst.append(_create_command('ccode', 'idea.idea_clion'))
    rst.append(_create_command('icode', 'idea.idea_intellij'))
    rst.append(_create_command('wcode', 'idea.idea_webstorm'))
    rst.append(_create_command('hcode', 'idea.idea_phpstorm'))
    return rst


setup(
    name='python shell util',
    version='1.0.0',
    description='shell 简单工具',
    entry_points={
        'console_scripts': _get_scripts()
    }
)
