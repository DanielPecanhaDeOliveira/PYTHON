from itertools import product

chars  = [chr(i) for i in range(97, 123)]
chars += [chr(i) for i in range(65, 91)]
chars += [chr(i) for i in range(48, 58)]



password = 'gatos'
tentativa = 0

def bruteForce_1(chars, password, lenPass):
    tentativa = 0

    for i in product(chars, repeat=lenPass):
        combina = ''.join(i)
        tentativa += 1
    
        if (tentativa % 500000 == 0):
            print('%10i --> %s' % (tentativa, combina))

        if password == combina:
            return('Senha encontrada é "{}", após {} tentativas.'.format(combina, tentativa))

    return ('Senha NÃO encontrada')

def bruteForce_2(chars, password, lenPass, comb_anterior = ''):
    global tentativa

    for LETRA in chars:
        combina = comb_anterior + LETRA
        tentativa += 1
        if (tentativa % 500000 == 0):
            print('%10i --> %s' % (tentativa, combina))

        if password == combina:
            print('Senha encontrada é "{}", após {} tentativas.'.format(combina, tentativa))
            #return 'ok'
            exit()

        elif (lenPass != 1):
            # E aqui a chamada da recursividade
            bruteForce_2(chars, password, lenPass-1, combina)

print(bruteForce_1(chars, password, lenPass=4))
print('*' * 60 + '\n')

print(bruteForce_2(chars, password, len(password)))
print('*' * 60 + '\n')

print(bruteForce_2(chars, 'cabo', 4))
print('*' * 60 + '\n')

print(bruteForce_2(chars, 'cabo', 5))

# Fim