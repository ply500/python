'''
Exemplos de print com ANSI Escape Code

\
033 -> ESC in ASCII octal 
[ ->Início do Escape Code


'''

print("\033[0;32m Green Color, normal\n")
print("\033[1;32m Green Color, bold\n")
print("\033[2;32m Green Color, faint\n")
print("\033[3;32m Green Color, italic\n")
print("\033[4;32m Green Color, underline\n")
print("\033[5;32m Green Color, underline\033[0m\n")

print("\033[1;32m Green Color, normal\n")


# print("\033[1;34m Blue Color\n")
# print("\033[2;32;40m Bright Green \n")
# print("\033[3;31m Red \033[0m\n")