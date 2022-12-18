import menu, os
from colorama import Fore, Back
Border1 = '════════════════════════════════════════════════════════════════════════'
border2 = '────────────────────────────────────────────────────────────────────────'
def Header(header_text):
      global Border1, border2
      print(Fore.BLUE + f'{Border1}\n' +
            Fore.WHITE + f'   {header_text}\n' +
            Fore.BLUE + border2 + Fore.RESET)
def botom():
      print(Fore.BLUE + Border1 + Fore.RESET)
def menu_list(menu):
      res = ''
      for i in range(len(menu)):
            if i < len(menu)-1:
                  res = res + '  ' + menu[i] + '\n'
            else:
                  res = res + '  ' + menu[i]
      return res

def show_menu(name, menulist):
      os.system('cls')
      Header(name)
      print(Fore.YELLOW + menu_list(menulist) + Fore.RESET)
      botom()

def print_result(header, res):
      global Border1, border2
      os.system('cls')
      print(Fore.GREEN + Border1 + Fore.RESET)
      print('  ' + header)
      print(Fore.GREEN + border2 + Fore.RESET)
      print(res)
      print(Fore.GREEN + Border1 + Fore.RESET)

