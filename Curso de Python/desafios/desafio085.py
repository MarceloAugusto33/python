numeros = []
par = []
impar = []
for c in range(0,7):
    n = int(input("Numero: "))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
par.sort()
impar.sort()
numeros.append(par[:])
numeros.append(impar[:])
print(numeros)
print("-"*30)
print(f"Os valores pares sao: {numeros[0]}")
print(f"Os valores impares: {numeros[1]}")
