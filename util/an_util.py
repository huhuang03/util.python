import subprocess
import time
import os

import argparse


def _command_push_cert(sub_parser):
    # sub_parser.add_argument("")
    pass


def get_sign(args):
    apk_path = os.path.abspath(args.apk_file)
    if not os.path.exists(apk_path):
        exit(f"apk is not exist {apk_path}")
    os.system(f"keytool -printcert -jarfile {apk_path}")


def screenshot():
    os.system('adb shell screencap -p /sdcard/tmp.jpg')

    file_path = str(round(time.time() * 1000)) + ".jpg"
    os.system(f'adb pull /sdcard/tmp.jpg {file_path}')
    print("Done!")


def main():
    parser = argparse.ArgumentParser(description="android utils")

    subparser = parser.add_subparsers(dest="command")
    push_cert = subparser.add_parser("push_cert", help="push cert file to system cert location(with rename it)")
    push_cert.add_argument("cert_file", type=str, help="cert file(like charlese cert file)")

    subparser.add_parser("screenshot", help="take a screenshot save name as current time milliseconds.")

    parser_get_sign = subparser.add_parser("get_sign", help="get sign info from apk file")
    parser_get_sign.add_argument("apk_file", type=str, help="print apk sign info")

    args = parser.parse_args()
    if args.command == "screenshot":
        screenshot()
    elif args.command == "get_sign":
        get_sign(args)


if __name__ == "__main__":
    main()
