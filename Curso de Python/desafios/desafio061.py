primeiro = int(input("primeiro termo: "))
razao = int(input("Digite a razao: "))
lista = []
lista.append(primeiro)
contador = 0
termos = 1
total = 0
while contador < 9:
    primeiro = primeiro + razao
    lista.append(primeiro)
    contador = contador + 1
total1 = contador
print(lista)
while termos != 0:
    termo = str(input("Voce Quer adicionar mais termos: [S]/[N]: ")).strip().upper()
    if termo == "S":
        termos = int(input("Digite qts termos quer add: "))
        contador = 0
        while contador < termos:
            primeiro = primeiro + razao
            lista.append(primeiro)
            contador += 1
    else:
        print("Fim do Programa!!")
        termos = 0
    total = total + termos
total = total + total1
print(lista)
print("Total de valores mostrados {}".format(total))