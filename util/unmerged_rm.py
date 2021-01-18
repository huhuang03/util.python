import os

def main():
    branch = os.system("git branch")
    print(branch)
    merged = os.system("git branch --merged")
    print(merged)