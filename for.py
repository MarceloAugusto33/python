lista = []
nlist = list(range(8))
bt0 = 0
bt1 = 0
for contador in nlist:
    bits = int(input("digite um bit: "))
    while bits < 0 or bits > 1:
        print("Voce nao pode colocar numero diferente de 0 e 1")
        bits = int(input("digite um bit: "))
    lista.append(bits)
    if bits == 0:
        bt0 = bt0 + 1
    else:
        bt1 = bt1 +1
print(lista)
print("essa byte contem", bt0, "de 0 e", bt1, "de 1")
