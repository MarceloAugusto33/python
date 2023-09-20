qidade = qHomem = qMulher = pessoa = 0
print("-"*30)
print("Castre uma pessoa")
print("-"*30)
while True:
    idade = int(input("Idade: "))
    sexo = input("[M] ou [F]: ").strip().upper()
    while sexo != "M" and sexo != "F":
        print("Comando invalido!")
        sexo = input("[M] ou [F]: ").strip().upper()
    print("-"*30)
    op = input("Quer continuar: [S] ou [N]").upper().strip()
    while op != "S" and op != "N":
        print("Comando invalido!")
        op = input("Quer continuar: [S] ou [N]").upper()
    if idade > 18:
        qidade += 1
    if sexo == "M":
        qHomem +=1
    if sexo == "F" and idade < 20:
        qMulher += 1
    pessoa += 1
    if op == "N":
        print("-"*30)
        print("Fim do Programa!!!")
        print("-"*30)
        break
print(f"Total de maiores de 18: {qidade}")
print(f"Homems cadrastados: {qHomem}")
print(f"Mulheres com menos de 20: {qMulher}")
print(f"Quantidade de Pessoas cadastradas: {pessoa}")


