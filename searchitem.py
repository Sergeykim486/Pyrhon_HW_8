import menu, os, functions, opensave
from colorama import Fore, Back

def findobject(searchobj, indata):
    findedid = []
    templist = []
    for i in indata:
        for j in i:
            if j == 'job_title':
                jobtitles = opensave.openjsonfile('jobtitle.json')
                for item in jobtitles:
                    if i[j] == item['id']:
                        if str(searchobj) in str(i[j]): # str(j).find(object) != -1:
                            if checkid(i['id'], templist) == 0:
                                templist.append(i['id'])
            elif j == 'department':
                departments = opensave.openjsonfile('department.json')
                for item in departments:
                    if i[j] == item['id']:
                        if str(searchobj) in str(i[j]): #  str(j).find(object) != -1:
                            if checkid(i['id'], templist) == 0:
                                templist.append(i['id'])
            elif str(searchobj) in str(i[j]): #  str(j).find(object) != -1:
                if checkid(i['id'], templist) == 0:
                    templist.append(i['id'])
    findedid = findbyid(indata, templist)
    return functions.genlist(findedid)

def findbyid(data, ids):
    res = []
    for i in ids:
        for item in data:
            if item['id'] == i:
                res.append(item)
    return res

def checkid(obj, data):
    finded = 0
    for i in data:
        if i == obj:
            finded = 1
    return finded

def getitembyid(data, id):
    for item in data:
        if item['id'] == id:
            return item