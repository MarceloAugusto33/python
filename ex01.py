bits = 0
lista= []
bt0= 0 
bt1 = 0
while bits < 8:
    bt = int(input("Digite os bits"))
    bits = bits + 1
    lista.append(bt)
    if bt == 0:
        bt0 = bt0 + 1
    else:
        bt1 = bt1 +1
print(lista)
print("essa byte contem", bt0, "de 0 e", bt1, "de 1")

