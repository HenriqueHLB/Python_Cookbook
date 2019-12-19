import random


n1 = input('Primeiro nome do ship: ')
n2 = input('Segundo nome: ')

chance0 = '[----------]'
chance10 = '[█---------]'
chance20 = '[██--------]'
chance30 = '[███-------]'
chance40 = '[████------]'
chance50 = '[█████-----]'
chance60 = '[██████----]'
chance70 = '[███████---]'
chance80 = '[████████--]'
chance90 = '[█████████-]'
chance100 = '[██████████]'
chance = random.randint(0, 100)

if chance == 100:
    print(f'Chance: {chance}% - {chance100}')
if chance <= 99 and chance >= 90:
    print(f'Chance: {chance}% - {chance90}')
if chance <= 89 and chance >= 80:
    print(f'Chance: {chance}% - {chance80}')
if chance <= 79 and chance >= 70:
    print(f'Chance: {chance}% - {chance70}')
if chance <= 69 and chance >= 60:
    print(f'Chance: {chance}% - {chance60}')
if chance <= 59 and chance >= 50:
    print(f'Chance: {chance}% - {chance50}')
if chance <= 49 and chance >= 40:
    print(f'Chance: {chance}% - {chance40}')
if chance <= 39 and chance >= 30:
    print(f'Chance: {chance}% - {chance30}')
if chance <= 29 and chance >= 20:
    print(f'Chance: {chance}% - {chance20}')
if chance <= 19 and chance >= 10:
    print(f'Chance: {chance}% - {chance10}')
if chance == 0:
    print(f'Chance: {chance}% - {chance0}')