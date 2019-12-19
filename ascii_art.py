from pyfiglet import Figlet


texto = input('Texto: ')
f = Figlet(font='slant')

print(f.renderText(texto))