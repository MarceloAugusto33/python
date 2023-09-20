numero = int(input("Digite o numero que voce quer ver a tabuada: "))
vezes = int(input("Ate quanto?: "))
for c in range(1 , vezes+1):
    print(" {} x {} = {}".format(numero,c,numero*c))
print("Fim da tabuada")