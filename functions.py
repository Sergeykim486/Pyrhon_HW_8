import opensave

def genlist(data):
    res = []
    for i in data:
        line = ''
        for j in i:
                if j == 'id':
                    line = line + ' ' + str(i[j]).ljust(4)
                elif j == 'f_name':
                    line = line + ' ' + str(i[j]).ljust(12)
                elif j == 'l_name':
                    line = line + ' ' + str(i[j]).ljust(12)
                elif j == 'name':
                    line = line + ' ' + str(i[j]).ljust(12)
        res.append(line)
    return res

def genlist2(data):
    res = []
    for i in data:
        line = ''
        for j in i:
            line = line + str(i[j]) + ' '
        res.append(line)
    return res