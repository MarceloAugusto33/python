numero = int(input("Digite um numero inteiro: "))
div = 0
for c in range(1, numero+1):
    if numero % c == 0:
        div += 1
        print("\033[42m{}\033[m".format(c))
    else:
         print("\033[41m{}\033[m".format(c))
if div > 2:
    print("Nao é primo")
else:
    print("Primo")