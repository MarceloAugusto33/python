print("="*30)
print("Caixa  Eletronico")
print("="*30)
cedula50 = cedula20 = cedula10 = cedula1 = 0
while True:
    valor = int(input("Quanto voce quer sacar: "))
    while valor >= 50:
        cedula50 += 1
        valor = valor - 50
    while valor >= 20 and valor < 50:
        cedula20 += 1
        valor = valor - 20
    while valor >= 10 and valor < 20:
        cedula10 += 1
        valor = valor - 10
    while valor >= 1 and valor < 10:
        cedula1 += 1
        valor = valor - 1
    if valor == 0:
        break
if cedula50 > 0:
    print(f"Notas de R$50: {cedula50}")
if cedula20 > 0:
    print(f"Notas de R$20: {cedula20}")
if cedula10 > 0:
    print(f"Notas de R$10: {cedula10}")
if cedula1 > 0:
    print(f"Notas de R$1: {cedula1}")