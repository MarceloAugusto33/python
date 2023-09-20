nome = str(input("Digite seu nome: "))
if nome == "Gustavo":
    print("Que nome bonito!")
elif nome == "Pedro" or nome == "Maria" or nome == "Paulo":
    print("seu nome é bem popular no Brasil")
else:
    print("seu nome é normal")
print("Tenha um bom dia {}".format(nome))