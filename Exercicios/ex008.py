#Conversor de medidas de comprimento
metros = float(input("Digite um valor em metros: "))
mm = metros * 1000
cm = metros * 100
dm = metros * 10
dam =  metros * 0.1
hm = metros * 0.01
km = metros * 0.001

print("{} metros equivale a {} milímetros, {} centímetros, {} decímetros, {} decâmetros, {} hectômetros e {} quilômetros. ".format(metros, mm, cm, dm, dam, hm, km))