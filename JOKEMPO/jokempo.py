#Recriando jogo JOKEMPO sem o uso de funções
import random
from time import sleep
#Criando cabeçalho
print('{:^30}'.format('\033[32mJOKEMPO\033[m'))
opçoes = ['PEDRA', 'PAPEL','TESOURA']
pc = random.choice(opçoes)
#Criando menu    
menu = ('''\n[0] PEDRA 
[1] PAPEl 
[2] TESOURA\n''')
print(menu)
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
        print('EMPATE!')
    if pc == 'PAPEL':
        print('O computador ganhou!')
    if pc == 'TESOURA':
        print('Você ganhou!')
if user == 1:
    if pc == 'PEDRA':
        print('Você ganhou!')
    if pc == 'PAPEL':
        print('EMPATE!')
    if pc == 'TESOURA':
        print('O computador ganhou!')
if user == 2:
    if pc == 'PEDRA':
        print('O computador ganhou!')
    if pc == 'PAPEL':
        print('Você ganhou!')
    if pc == 'TESOURA':
        print('EMPATE!')
print('\033[m='*25)

