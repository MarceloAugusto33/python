lista = []
for c in range(0,5):
    n = int(input("Numero: "))
    if c == 0 or n > lista[len(lista)-1]:
        lista.append(n)
        print("Adicionamos ao final da lista!")
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                print(f"Adicionado na posiçao {pos}")
                break
            pos += 1
print(lista)