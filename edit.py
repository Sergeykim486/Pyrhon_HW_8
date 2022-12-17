from colorama import Fore, Back
import os, sys, messagestouser, visual, searchitem, opensave, menu

def editmenu(h1, members, memid):
    while True:
        visual.show_menu(h1, menu.search_menu)
        choice = input('Выберите действие... ->  ')
        if choice.isdigit() == True:
            if int(choice) == 1:
                showmember(members, memid)
            elif int(choice) == 2:
                memberslist()
            elif int(choice) == 3:
                memberslist()
            elif int(choice) == 0:
                break
            else:
                messagestouser.errors()
        else:
            messagestouser.errors()

def showmember(data, id):
    textmes = ''
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

# def edititem(data, id):
#     for item in data:
#         if item['id'] == id:
            