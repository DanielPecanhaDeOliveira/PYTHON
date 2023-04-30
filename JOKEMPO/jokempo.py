#Recriando jogo JOKEMPO sem o uso de funções
import random
from time import sleep
#Criando cabeçalho
def cabeçalho(msg):
    linha('\033[31m', '\033[m')
    print(msg.center(32))
    linha('\033[31m', '\033[m')


def linha (abrecor, fechacor):
    print(f'{abrecor}={fechacor}' *25)


c = 1
while True:
    cabeçalho("\033[34mJOKENPÔ\033[m")
    opçoes = ['PEDRA', 'PAPEL','TESOURA']
    pc = random.choice(opçoes)
    #Criando menu
    menu = ('''\n[0] PEDRA 
[1] PAPEl 
[2] TESOURA\n''')
    print(menu)

    user = int(input('Qual vc escolhe? '))
    sleep(1)
    linha('\033[31m', '\033[m')
    #Mostrando as opções escolhidas
    print(f'O computador jogou {pc}')
    print(f'Você jogou {opçoes[user]} ')
    linha('\033[31m', '\033[m')
    sleep(2)
    c  += 1
    #Verificando o ganhador
    if user == 0:
        if pc == 'PEDRA':
            print('\033[33mEMPATE!\033[m'.center(30))
        if pc == 'PAPEL':
            print('\033[31mO computador ganhou!\033[m'.center(30))
        if pc == 'TESOURA':
            print('\033[32mVocê ganhou!\033[m'.center(30))
    if user == 1:
        if pc == 'PEDRA':
            print('\033[32mVocê ganhou!\033[m'.center(30))
        if pc == 'PAPEL':
            print('\033[33mEMPATE!\033[m'.center(30))
        if pc == 'TESOURA':
            print('\033[31mO computador ganhou!\033[m'.center(30))
    if user == 2:
        if pc == 'PEDRA':
            print('\033[31mO computador ganhou!\033[m'.center(30))
        if pc == 'PAPEL':
            print('\033[32mVocê ganhou!\033[m'.center(30))
        if pc == 'TESOURA':
            print('\033[33mEMPATE!\033[m'.center(30))
    print('\033[m='*25)
    sleep(1)
    cabeçalho(f"\033[34mRODADA\033[m \033[31m{c}\033[mº".center(42))
    sleep(1)


