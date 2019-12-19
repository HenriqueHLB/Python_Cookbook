from time import localtime
from pygame import mixer

h = int(input('Hora: '))
m = int(input('Minuto: '))


while True:
    if localtime().tm_hour == h and localtime().tm_min == m:
        print('Acordar!')
        mixer.init()
        mixer.music.load('despertador.mp3')
        mixer.music.play()
        x = input('Digite qualquer coisa para parar: ')
        mixer.music.stop()
        break