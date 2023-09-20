frase = input("Digite um frase: ").strip().upper()
lista = frase.split()
junto = ''.join(lista)
inverso = ""
for c in range(len(junto)-1,-1,-1):
    inverso = inverso + junto[c]
if inverso == junto:
    print("Frase é um palindromo")
    print(inverso)
    print(junto)
else:
    print("Nao é um palindromo")
    print(inverso)
    print(junto)
