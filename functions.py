import opensave

def genlist(data):
    res = []
    for i in data:
        line = ''
        for j in i:
            if j == 'job_title':
                jobtitles = opensave.openjsonfile('jobtitle.json')
                for item in jobtitles:
                    if ['id'] == j:
                        line = line + ' ' + item['name']
            elif j == 'department':
                departments = opensave.openjsonfile('department.json')
                for item in departments:
                    if ['id'] == j:
                        line = line + ' ' + item['name']
            else:
                line = line + ' ' + str(i[j])
        res.append(line)
    return res