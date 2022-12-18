from colorama import Fore, Back
import os, sys

def errors():
    os.system('cls')
    print(Fore.RED + '  ОШИБКА!!!\n НЕ ВЕРНЫЙ ВВОД ПОВТОРИТЕ ПОПЫТКУ.' + Fore.RESET)
    input('Чтобы продолжить нажмите [ENTER]...')

def errorm(m):
    os.system('cls')
    print(Fore.RED + f'  ОШИБКА!!!\n {m}' + Fore.RESET)
    input('Чтобы продолжить нажмите [ENTER]...')
    
def question(q):
    confirm = input(f'{q}\n  [y] - Да      [n] - Нет')
    confirm.replace('Y', 'y')
    confirm.replace('N', 'n')
    return confirm