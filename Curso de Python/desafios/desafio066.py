cont = soma = 0
while True:
    n = int(input("[999 para Parar] Digite o Numero: "))
    if n == 999:
        print("Programa Finalizado!")
        break
    cont += 1
    soma += n
print(f"Numeros digitados {cont} com a soma de {soma}")