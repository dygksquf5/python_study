from colorama import init

init()

from colorama import Fore, Back, Style

size = 11

for i in range(0, size):
    if i == 0:
        print(Fore.YELLOW + '*'.center(size, ' '))
    elif i % 2 == 0 and i > 0:
        print(Fore.GREEN + ('*' * i).center(size, ' '))
    else:
        print(Fore.RED + ("'" * (i+1)).center(size, " "))

init(autoreset=True)
print("")
print(Back.RED + "Merry".center(size + 2, ' '))
print(Back.BLUE + "Christmas!".center(size+2, ' '))
print(" ")