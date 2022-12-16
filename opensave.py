import json

def savetojson(fname, data):
    f = open('db/' + fname, 'w')
    f.write(json.dumps(data, indent=2))
    f.close

def openjsonfile(fname):
    f = open('db/' + fname, 'r')
    file = json.loads(f.read())
    res = file
    f.close()
    return res