a = int(input("Digite um numero: "))
b = int(input("digite outro numero: "))
c = int(input("Digite mais um numero: "))
d = int(input("Digite o ultimo numero: "))
tupla = (a,b,c,d)
print(f"Valores digitados: {tupla}")
print(f"o valor 9 apareceu {tupla.count(9)} vez")
if 3 not in tupla:
    print("valor 3 nao foi enserido!")
else:
    print(f"O valor 3 aparceu na pociçao {tupla.index(3)+1}")
for c in tupla:
    if c % 2 ==0:
        print(f"valor par: {c}",end=" ")
