import requests
import pyperclip
import json

URL = "https://api.studytime.xin/activationCode"


def main():
    content = requests.get(URL).content
    j_content = json.loads(content)
    code = j_content['data']
    print(code)
    print('already copied to system clipboard')
    pyperclip.copy(code)
