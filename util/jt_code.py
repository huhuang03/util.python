import requests
import pyperclip
import json

# IntellJ IDEA ������ ÿ�ո��� �����ṩ��JetBrainsȫ��Ͱ������ - �׳���Ա����ϰ��
# https://www.studytime.xin/article/code.html

URL = "https://api.studytime.xin/activationCode"


def main():
    content = requests.get(URL).content
    j_content = json.loads(content)
    code = j_content['data']
    print(code)
    print('already copied to system clipboard')
    pyperclip.copy(code)
