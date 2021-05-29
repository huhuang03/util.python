import requests
import pyperclip
import json

# IntellJ IDEA 激活码 每日更新 长期提供【JetBrains全家桶】可用 - 白程序员的自习室
# https://www.studytime.xin/article/code.html

URL = "https://api.studytime.xin/activationCode"


def main():
    content = requests.get(URL).content
    j_content = json.loads(content)
    code = j_content['data']
    print(code)
    print('already copied to system clipboard')
    pyperclip.copy(code)
