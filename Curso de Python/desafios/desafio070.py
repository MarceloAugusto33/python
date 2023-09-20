total = m1000 = contador = menorp = menorm = 0
while True:
    nome = str(input("Nome Produto: "))
    preço = float(input("Digite o valor: R$"))
    op = input("Adicionar Produto?: [S] ou [N]: ").strip().upper()
    while op != "S" and op != "N":
        print("Comando Invalido!")
        op = input("Adicionar Produto?: [S] ou [N]: ").strip().upper()
    total += preço
    if preço > 1000:
        m1000 +=1
    contador += 1
    if contador == 1:
        menorp = preço
        menorm = nome
    else:
        if preço < menorp:
            menorp = preço
            menorm = nome
    if op =="N":
        print("\033[42mLista de Compras Finalizada!\033[m")
        break
print("-"*30)
print("Fim do programa")
print("-"*30)
print(f"Total gasto: {total}")
print(f"Produtos Que custam mais de 1000: {m1000}")
print(f"O produto mais barato foi o {menorm} com valor de R${menorp}")

    



    