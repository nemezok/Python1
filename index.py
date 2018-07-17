#from colorama import init
from colorama import Fore, Back, Style
#init()

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

print('{blue}Hello, World!{endcolor}'.format(blue='\033[96m', endcolor='\033[0m')) #print('\033[96mHello, World!\033[0m')
print(Fore.BLUE + 'Hello, World!')