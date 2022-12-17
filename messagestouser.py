from colorama import Fore, Back
import os, sys

def errors():
    os.system('cls')
    print(Fore.RED + '  ОШИБКА!!!\n НЕ ВЕРНЫЙ ВВОД ПОВТОРИТЕ ПОПЫТКУ.' + Fore.RESET)
    input('Чтобы продолжить нажмите [ENTER]...')