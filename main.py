import edit, menu, messagestouser, opensave, visual, os, functions, sys, searchitem
from colorama import Fore, Back

members = opensave.openjsonfile('comembers.json')
jobtitles = opensave.openjsonfile('jobtitle.json')
departments = opensave.openjsonfile('department.json')

def main():
    global members, jobtitles, departments
    while True:
        visual.show_menu(' Г Л А В Н О Е   М Е Н Ю ', menu.main_menu)
        choice = input('Выберите действие... ->  ')
        if choice.isdigit() == True:
            if int(choice) == 1:
                memberslist()
            elif int(choice) == 0:
                sys.exit()
            else:
                messagestouser.errors()
        else:
            messagestouser.errors()

def memberslist():
    global members, jobtitles, departments
    while True:
        visual.show_menu(' С О Т Р У Д Н И К И ', menu.edit_menu)
        choice = input('Выберите действие... ->  ')
        if choice.isdigit() == True:
            if int(choice) == 0:
                main()
            elif int(choice) == 1:
                visual.print_result(' С О Т Р У Д Н И К И -> ПОЛНЫЙ СПИСОК', visual.menu_list(searchitem.findobject('', members)))
                memid = int(input('Выберите позицию... ->  '))
                selectedmember = searchitem.getitembyid(members, memid)
                h1 = str(selectedmember['f_name']) + ' ' + str(selectedmember['l_name'])
                edit.editmenu(h1, members, memid)
            elif int(choice) == 2:
                visual.print_result(' С О Т Р У Д Н И К И -> ПОИСК', 'Для поиска объекта,\nвведите имя, фамилию, должность или подразделение...')
                visual.print_result(' С О Т Р У Д Н И К И -> РЕЗУЛЬТАТ ПОИСКА', visual.menu_list(searchitem.findobject(input('Введите текст ->  '), members)))
                memid = int(input('Выберите позицию... ->  '))
                selectedmember = searchitem.getitembyid(members, memid)
                h1 = str(selectedmember['f_name']) + ' ' + str(selectedmember['l_name'])
                edit.editmenu(h1, members, memid)
            else:
                messagestouser.errors()
        else:
            messagestouser.errors()



main()