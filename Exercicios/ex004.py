#Algoritmo de tipos primitivos
algo = input("Digite algo: ")
print("O tipo primitivo desse valor é : ", type(algo))
print("Só tem espaços: ", algo.isspace())
print("É um número: ", algo.isalnum())
print("É alfabético: ", algo.isalpha())