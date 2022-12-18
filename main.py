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
            elif int(choice) == 4:
                opensave.savetojson('comembers.json', members)
                opensave.savetojson('jobtitle.json', jobtitles)
                opensave.savetojson('department.json', departments)
                visual.print_result('Сохранение завершено', 'Данные сохранены...')
                input('Чтобы продолжить нажмите [ENTER]...')
            elif int(choice) == 2:
                jobt()
            elif int(choice) == 3:
                depart()
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
                memid = input('Выберите позицию... ->  ')
                if memid.isdigit() == False:
                    messagestouser.errors()
                else:
                    selectedmember = searchitem.getitembyid(members, int(memid))
                    h1 = str(selectedmember['f_name']) + ' ' + str(selectedmember['l_name'])
                    edit.editmenu(h1, members, int(memid), 1)
            elif int(choice) == 2:
                visual.print_result(' С О Т Р У Д Н И К И -> ПОИСК', 'Для поиска объекта,\nвведите имя, фамилию, должность или подразделение...')
                visual.print_result(' С О Т Р У Д Н И К И -> РЕЗУЛЬТАТ ПОИСКА', visual.menu_list(searchitem.findobject(input('Введите текст ->  '), members)))
                memid = input('Выберите позицию... ->  ')
                if memid.isdigit() == False:
                    messagestouser.errors()
                else:
                    selectedmember = searchitem.getitembyid(members, int(memid))
                    h1 = str(selectedmember['f_name']) + ' ' + str(selectedmember['l_name'])
                    edit.editmenu(h1, members, int(memid), 1)
            elif int(choice) == 3:
                edit.newitem(members)
            else:
                messagestouser.errors()
        else:
            messagestouser.errors()

def jobt():
    global members, jobtitles, departments
    while True:
        visual.show_menu(' Д О Л Ж Н О С Т И ', menu.edit_menu)
        choice = input('Выберите действие... ->  ')
        if choice.isdigit() == True:
            if int(choice) == 0:
                main()
            elif int(choice) == 1:
                visual.print_result(' Д О Л Ж Н О С Т И -> ПОЛНЫЙ СПИСОК', visual.menu_list(searchitem.findobject('', jobtitles)))
                memid = input('Выберите позицию... ->  ')
                if memid.isdigit() == False:
                    messagestouser.errors()
                else:
                    selectedmember = searchitem.getitembyid(jobtitles, int(memid))
                    h1 = str(selectedmember['name'])
                    edit.editmenu(h1, jobtitles, int(memid), 2)
            elif int(choice) == 2:
                visual.print_result(' Д О Л Ж Н О С Т И -> ПОИСК', 'Для поиска объекта,\nвведите наименование или его часть...')
                visual.print_result(' Д О Л Ж Н О С Т И -> РЕЗУЛЬТАТ ПОИСКА', visual.menu_list(searchitem.findobject(input('Введите текст ->  '), jobtitles)))
                memid = input('Выберите позицию... ->  ')
                if memid.isdigit() == False:
                    messagestouser.errors()
                else:
                    selectedmember = searchitem.getitembyid(jobtitles, int(memid))
                    h1 = str(selectedmember['f_name']) + ' ' + str(selectedmember['l_name'])
                    edit.editmenu(h1, jobtitles, int(memid), 2)
            elif int(choice) == 3:
                edit.newitem(jobtitles)
            else:
                messagestouser.errors()
        else:
            messagestouser.errors()

def depart():
    global members, jobtitles, departments
    while True:
        visual.show_menu(' Д О Л Ж Н О С Т И ', menu.edit_menu)
        choice = input('Выберите действие... ->  ')
        if choice.isdigit() == True:
            if int(choice) == 0:
                main()
            elif int(choice) == 1:
                visual.print_result(' Д О Л Ж Н О С Т И -> ПОЛНЫЙ СПИСОК', visual.menu_list(searchitem.findobject('', departments)))
                memid = input('Выберите позицию... ->  ')
                if memid.isdigit() == False:
                    messagestouser.errors()
                else:
                    selectedmember = searchitem.getitembyid(departments, int(memid))
                    h1 = str(selectedmember['name'])
                    edit.editmenu(h1, departments, int(memid), 2)
            elif int(choice) == 2:
                visual.print_result(' Д О Л Ж Н О С Т И -> ПОИСК', 'Для поиска объекта,\nвведите наименование или его часть...')
                visual.print_result(' Д О Л Ж Н О С Т И -> РЕЗУЛЬТАТ ПОИСКА', visual.menu_list(searchitem.findobject(input('Введите текст ->  '), jobtitles)))
                memid = input('Выберите позицию... ->  ')
                if memid.isdigit() == False:
                    messagestouser.errors()
                else:
                    selectedmember = searchitem.getitembyid(departments, int(memid))
                    h1 = str(selectedmember['f_name']) + ' ' + str(selectedmember['l_name'])
                    edit.editmenu(h1, departments, int(memid), 2)
            elif int(choice) == 3:
                edit.newitem(departments)
            else:
                messagestouser.errors()
        else:
            messagestouser.errors()

main()