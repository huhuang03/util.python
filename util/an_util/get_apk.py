import os
import re
import subprocess


def get_apk(args):
    pkg_name = args.pkg_name
    commands = ["adb", "shell", "pm", "path", pkg_name]
    r_stdout = subprocess.run(commands, stdout=subprocess.PIPE).stdout
    if not r_stdout:
        exit(f"Please check app {pkg_name} exist")
    apk_inner_path = r_stdout.decode("utf-8").strip()
    apk_inner_path = re.search(re.compile("package:(.*)"), apk_inner_path).group(1)
    print(apk_inner_path)
    output_name = f"{pkg_name}.apk"
    if os.path.exists(output_name):
        exit(f"file {output_name} already exist")
    os.system(f"adb pull {apk_inner_path} {output_name}")