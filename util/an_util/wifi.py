import os
import subprocess

_PORT = 5555

def wifi():
    """
    follow https://stackoverflow.com/questions/4893953/run-install-debug-android-applications-over-wi-fi
    adb via wifi
    """
    ip_output = subprocess.run(["adb", "shell", "ip" "-f" "inet" "addr" "show"], stdout=subprocess.PIPE).stdout.decode("utf-8")
    print(ip_output)
    os.system(f"adb tcpip {_PORT}")