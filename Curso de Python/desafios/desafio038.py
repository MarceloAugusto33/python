n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
if n1 > n2:
    print("O primeiro valor {} é maior que o valor {}".format(n1,n2))
elif n1 == n2:
    print("O valor {} é igual ao valor {}".format(n1,n2))
else:
    print("O segundo valor {} é maior que o valor {}".format(n2,n1))