nome = str(input("Digite seu nome completo: ")).strip()
lista = nome.split()
print(lista)
print("Muito prazer em te conhecer!")
print("Seu primeiro nome é {}".format(lista[0]))
print("Seu ultimo nome é {}".format(lista[len(lista)-1]))