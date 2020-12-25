from colorama import Fore,Back,Style
import colorsys

print(Fore.BLACK + 'some red text')
print(Back.BLUE + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')