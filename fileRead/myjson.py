import json

def readJson():
    with open('/Users/palm/Desktop/programmazione/Python/scripting/socket/fileRead/writeParam.json','r') as file:
        read = json.load(file)
        return read
