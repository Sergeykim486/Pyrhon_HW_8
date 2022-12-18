from colorama import Fore, Back
import os, sys, messagestouser, visual, searchitem, opensave, menu, functions

def editmenu(h1, item, selectecid, flag):
    while True:
        visual.show_menu(h1, menu.search_menu)
        choice = input('Выберите действие... ->  ')
        if choice.isdigit() == True:
            if int(choice) == 1:
                showmember(item, selectecid)
            elif int(choice) == 2:
                if flag == 1:
                    edititem(item, selectecid)
                elif flag == 2:
                    changesinglitem(item, selectecid)
            elif int(choice) == 3:
                removeitem(item, selectecid)
            elif int(choice) == 0:
                break
            else:
                messagestouser.errors()
        else:
            messagestouser.errors()

def showmember(data, id):
    textmes = ''
    if id == 0:
        for i in data:
            if i == 'job_title':
                jobtitle = searchitem.getitembyid(opensave.openjsonfile('jobtitle.json'), data[i])
                textmes = textmes + str(i).ljust(12) + ' ' + str(jobtitle['name']).ljust(12) + '\n'
            elif i == 'department':
                dep = searchitem.getitembyid(opensave.openjsonfile('department.json'), data[i])
                textmes = textmes + str(i).ljust(12) + ' ' + str(dep['name']).ljust(12) + '\n'
            else:
                textmes = textmes + str(i).ljust(12) + ' ' + str(data[i]).ljust(12) + '\n'
        visual.print_result('Карточка сотрудника:', textmes)
    else:
        for item in data:
            if item['id'] == id:
                for i in item:
                    if i == 'job_title':
                        jobtitle = searchitem.getitembyid(opensave.openjsonfile('jobtitle.json'), item[i])
                        textmes = textmes + str(i).ljust(12) + ' ' + str(jobtitle['name']).ljust(12) + '\n'
                    elif i == 'department':
                        dep = searchitem.getitembyid(opensave.openjsonfile('department.json'), item[i])
                        textmes = textmes + str(i).ljust(12) + ' ' + str(dep['name']).ljust(12) + '\n'
                    else:
                        textmes = textmes + str(i).ljust(12) + ' ' + str(item[i]).ljust(12) + '\n'
        visual.print_result('Карточка сотрудника:', textmes)
    input('Чтобы продолжить нажмите [ENTER]...')

def edititem(data, id):
    for item in data:
        if item['id'] == id:
            while True:
                visual.show_menu(item['f_name'] + ' ' + item['l_name'], menu.editmember)
                choice = input('Выберите действие... ->  ')
                if choice.isdigit() == True:
                    if 0 < int(choice) < 8:
                        changed = changeitem(int(choice), item)
                        if changed != False:
                            save(item, changed)
                    elif int(choice) == 0:
                        break
                    else:
                        messagestouser.errors()
                else:
                    messagestouser.errors()

def save(item, changed):
    for i in item:
        item[i] = changed[i]

def changesinglitem(item, id):
    for i in item:
        if i['id'] == id:
            for j in i:
                if j != 'id':
                    i[j] = input(f'Введите {str(j)} ->  ')

def changeitem(choice, item):
    curindex = 0
    for i in item:
        if choice == curindex or choice == 7:
            if i != 'id':
                if i == 'job_title':
                    visual.show_menu('Должности', functions.genlist(opensave.openjsonfile('jobtitle.json')))
                    item[i] = int(input('Выберите должность... ->  '))
                elif i == 'department':
                    visual.show_menu('Структурные подразделения', functions.genlist(opensave.openjsonfile('department.json')))
                    item[i] = int(input('Выберите структурное подразделение... ->  '))
                else:
                    item[i] = input(f'Введите {str(i)} ->  ')
        curindex += 1
    showmember(item, 0)
    confirm = messagestouser.question('Подтвердите введенную информацию:')
    if confirm == 'y':
        return item
    elif confirm == 'n':
        return False

def newmember(members):
    newmem = {
        'id': 0,
        'f_name': '',
        'l_name': '',
        'phone': '',
        'email': '',
        'job_title': 0,
        'department': 0
        }
    for i in newmem:
        if i == 'id':
            newmem[i] = len(members)+1
        elif i == 'job_title':
            visual.show_menu('Должности', functions.genlist(opensave.openjsonfile('jobtitle.json')))
            newmem[i] = int(input('Выберите должность... ->  '))
        elif i == 'department':
            visual.show_menu('Структурные подразделения', functions.genlist(opensave.openjsonfile('department.json')))
            newmem[i] = int(input('Выберите структурное подразделение... ->  '))
        else:
            newmem[i] = input(f'Введите {str(i)} ->  ')
    showmember(newmem, 0)
    confirm = messagestouser.question('Подтвердите введенную информацию:')
    if confirm == 'y':
        members.append(newmem)
        return newmem
    elif confirm == 'n':
        return False

def newitem(items):
    newmem = {}
    flag = 0
    for item in items:
        if flag == 0:
            for k in item:
                if str(item[k]).isdigit == True:
                    newmem[k] = 0
                else:
                    newmem[k] = ''
        flag = 1
    for i in newmem:
        if i == 'id':
            newmem[i] = len(items)+1
        elif i == 'job_title':
            visual.show_menu('Должности', functions.genlist(opensave.openjsonfile('jobtitle.json')))
            newmem[i] = int(input('Выберите должность... ->  '))
        elif i == 'department':
            visual.show_menu('Структурные подразделения', functions.genlist(opensave.openjsonfile('department.json')))
            newmem[i] = int(input('Выберите структурное подразделение... ->  '))
        else:
            newmem[i] = input(f'Введите {str(i)} ->  ')
    showmember(newmem, 0)
    confirm = messagestouser.question('Подтвердите введенную информацию:')
    if confirm == 'y':
        items.append(newmem)
        return newmem
    elif confirm == 'n':
        return False

def removeitem(items, itemid):
    for i in items:
        if i['id'] == itemid:
            q = messagestouser.question('Вы уверены что хотите удалить этот объект?')
            if q == 'y':
                items.remove(i)