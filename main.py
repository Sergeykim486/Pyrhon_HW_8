import edit, menu, messagestouser, opensave, search, visual, os, functions, sys
from colorama import Fore, Back

members = opensave.openjsonfile('comembers.json')
jobtitles = opensave.openjsonfile('jobtitle.json')
departments = opensave.openjsonfile('department.json')

def errors():
    os.system('cls')
    print(Fore.RED + '  ОШИБКА!!!\n НЕ ВЕРНЫЙ ВВОД ПОВТОРИТЕ ПОПЫТКУ.' + Fore.RESET)
    input('Чтобы продолжить нажмите [ENTER]...')

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
                errors()
        else:
            errors()

def memberslist():
    global members, jobtitles, departments
    while True:
        visual.show_menu(' С О Т Р У Д Н И К И ', menu.edit_menu)
        choice = input('Выберите действие... ->  ')
        if choice.isdigit() == True:
            if int(choice) == 0:
                main()
            elif int(choice) == 1:
                visual.print_result(' С О Т Р У Д Н И К И -> ПОЛНЫЙ СПИСОК', visual.menu_list(functions.genlist(members)))
                input('Чтобы продолжить нажмите [ENTER]...')
            else:
                errors()
        else:
            errors()



main()