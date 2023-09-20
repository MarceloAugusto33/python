contador = 0
acumulador = 0
n = 0
while n != 999:
    n = int(input("Digite um numero[999 para parar]: "))
    if n != 999:
        contador += 1
        acumulador += n
print("Fim do programa!")
print("Quantidade de numeros digitados: {}".format(contador))
print("A soma de todos esses numeros: {}".format(acumulador))

