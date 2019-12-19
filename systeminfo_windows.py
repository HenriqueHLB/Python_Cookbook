import platform
import os
import sys
import psutil
import datetime


print('Portas abertas: ')
os.system('netstat -aon')

print('Adaptadores de rede: ')
os.system('ipconfig')

os.system('schtasks')

print('\n')

print(f'Sistema operacional: {platform.system()} ({platform.platform()})')

print(f'Versão: {platform.release()} ({platform.version()})')

print(f'Arquitetura: {platform.architecture()[0]}')

print(f'Tipo de máquina: {platform.machine()}')

print(f'Nome da rede do computador: {platform.node()}')

print(f'Inicialização do sistema: {datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%d-%m-%Y %H:%M:%S")}')

print('Usuários do sistema: ', end='')
usuários = []
for x in range(len(psutil.users())):
    usuários.append(psutil.users()[x].name)
print(' - '.join(usuários))

print(f'Processador: {platform.processor()}')
print(f'Quantidade de CPUs: {os.cpu_count()}')
print(f'Utiilização da CPU: {psutil.cpu_percent()}%')
print(f'Frequência da CPU: {psutil.cpu_freq().current}MHz')

try:
    print(f'Espaço total de disco: {psutil.disk_usage("/").total} bytes')
    print(f'Espaço de disco usado: {psutil.disk_usage("/").used} bytes ({psutil.disk_usage("/").percent}%)')
    print(f'Espaço de disco livre: {psutil.disk_usage("/").free} bytes')
except:
    pass

print(f'Memória virtual total: {psutil.virtual_memory().total} bytes')
print(f'Memória virtual disponível: {psutil.virtual_memory().available} bytes')

print('Partições do sistema: ', end='')
partições = []
for x in range(len(psutil.disk_partitions())):
    partições.append(psutil.disk_partitions()[x].device)
print(' - '.join(partições))

print(f'Bateria disponível: {psutil.sensors_battery().percent}%')
if psutil.sensors_battery().power_plugged == True:
    print('Carregando: sim')
elif psutil.sensors_battery().power_plugged == False:
    print(f'Bateria restante em segundos: {psutil.sensors_battery().secsleft}')
    print('Carregando: não')