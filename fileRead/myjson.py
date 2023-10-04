import json

def readJson():
    path = input('Select file path: ')
    if not path:
        print('Invalid path')
        return
    with open(path,'r') as file:
        read = json.load(file)
        return read