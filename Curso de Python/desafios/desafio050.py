soma = 0
for numeros in range(0,6):
    n = int(input("digite um  numero: "))
    if n % 2 == 0:
        soma = soma + n
print("A soma deu {}".format(soma))