from colorama import init, Fore, Back, Style

init()

print(Fore.GREEN + "Зелений" + Style.RESET_ALL)
print(Fore.RED + Back.WHITE + Style.BRIGHT + "Червоний" + Style.RESET_ALL)

from colorama import Back
print(Back.YELLOW + "Жовтий" + Style.RESET_ALL)

from colorama import Style
print(Style.BRIGHT + "Яскравий" + Style.RESET_ALL)