import argparse
import json

def parser_java(name, bean):
    rst = "class {} {".format(name)
    for k, v in bean.items():
        rst += "\tpublic String {}".format(k)
    rst += "}"
    return rst

def main():
    parser = argparse.ArgumentParser(description='convert json to bean')
    parser.add_argument('-l', type=str, choices=["java"], help="dist language")
    parser.add_argument('-n', type=str, help='the bean name')
    
    args = parser.parse_args()
    lang = args.l
    name = args.n
    if not lang or not name:
        parser.print_help
        exit(0)

    print("please input the json: ")
    json_content = []
    while True:
        line = input()
        json_content.append(line)
        if line == '':
            break

    json_content = "".join(json_content)
    print(json_content)
    try:
        bean = json.loads("".join(json_content))
    except:
        exit("illegal json:\n {}}".format(json_content))

    rst = parser_java(name, bean)
    print(rst)
    


    