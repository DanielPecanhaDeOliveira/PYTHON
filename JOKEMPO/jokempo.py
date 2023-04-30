#Recriando jogo JOKEMPO sem o uso de funções
import random
from time import sleep
#Criando cabeçalho
print('=' *20)
print('{:^30}'.format('\033[32mJOKENPÔ\033[m'))
print('=' *20)
opçoes = ['PEDRA', 'PAPEL','TESOURA']
pc = random.choice(opçoes)
#Criando menu    
menu = ('''\n[0] PEDRA 
[1] PAPEl 
[2] TESOURA\n''')
print(menu)
print('=' *20)
user = int(input('Qual vc escolhe? '))
sleep(1.5)
print('='*25)
#Mostrando as opções escolhidas
print(f'O computador jogou {pc}')
print(f'Você jogou {opçoes[user]} ')
print('='*25, '\n', end='\033[32m')
sleep(2)
#Verificando o ganhador 
if user == 0:
    if pc == 'PEDRA':
        print('\033[33mEMPATE!\033[m')
    if pc == 'PAPEL':
        print('\033[31mO computador ganhou!\033[m')
    if pc == 'TESOURA':
        print('Você ganhou!')
if user == 1:
    if pc == 'PEDRA':
        print('\033[32mVocê ganhou!\033[m')
    if pc == 'PAPEL':
        print('\033[33mEMPATE!\033[m')
    if pc == 'TESOURA':
        print('\033[31mO computador ganhou!\033[m')
if user == 2:
    if pc == 'PEDRA':
        print('\033[31mO computador ganhou!\033[m')
    if pc == 'PAPEL':
        print('Você ganhou!')
    if pc == 'TESOURA':
        print('\033[33mEMPATE!\033[m')
print('\033[m='*25)

