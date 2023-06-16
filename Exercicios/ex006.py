#Algoritmo q lê um número e mostra seu dobro, triplo e raiz quadrada.

num = int(input("Digite um número: "))
dobro = num * 2
triplo = num * 3
raizq = num ** (1/2) 
print("O dobro de {} é {}. ".format(num, dobro))
print("O triplo de {} é {}. ".format(num, triplo))
print("A raiz quadrada de {} é {:.2f}. ".format(num, raizq))

