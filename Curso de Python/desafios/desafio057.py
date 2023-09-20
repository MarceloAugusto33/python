sexo = str(input("Sexo [M] [F]: ")).strip().upper()
while sexo != "M" and sexo != "F":
    print("Comando invalido, digite novamente: ")
    sexo = str(input("Sexo [M] [F]: ")).strip().upper()
print("Fim do programa!")