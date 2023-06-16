#Calculo de m² de uma parede na condição de que 1 litro de tinta pinta uma área de 2m².
altura = float(input("Altura: "))
largura = float(input("Largura: "))
area = altura * largura 
print(f"Em uma parede de {area} m² você gastaria {area / 2} litros de tinta para pinta-la. ")