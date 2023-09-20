n1 = float(input("Digite o numero 1: "))
n2 = float(input("Digite o numero 2: "))
n3 = float(input("Digite o numero 3: "))
if n1 > n2 and n1 > n3:
    print("Maior é o {}".format(n1))
if n2 > n1 and n2 > n3:
    print("Maior é o {}".format(n2))
if n3 > n1 and n3 > n2:
    print("Maior é o {}".format(n3))
if n1 < n2 and n1 < n3:
    print("Menor é o {}".format(n1))
if n2 < n1 and n2 < n3:
    print("Menor é o {}".format(n2))
if n3 < n1 and n3 < n2:
    print("Menor é o {}".format(n3))