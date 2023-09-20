valor_compras = float(input("Qual valor das compras: "))
print('''========= Loja =========
[ 1 ] A vista dinheiro
[ 2 ] A vista cartao
[ 3 ] Em ate 2x no cartao
[ 4 ] 3x ou mais no cartao''')
opcao = int(input("Digite uma opçao acima: "))
if opcao == 1:
    preco = valor_compras - (valor_compras*(10/100))
    print("Valor avista da compra final ficou de R${}".format(preco))
elif opcao == 2:
    preco = valor_compras - (valor_compras*(5/100))
    print("Valor avista no cartao ficou de R${}".format(preco))
elif opcao == 3:
    preco = valor_compras / 2
    print("O valor 2x no cartao deu 2x R${}".format(preco))
elif opcao == 4:
    parcelas = int(input("Em quantas vezes voce quer parcelar: "))
    total = valor_compras + (valor_compras*(20/100))
    parcela = total / parcelas
    print("O valor em {}x no cartao deu {} vezes R${}".format(parcelas,parcelas,parcela))
else:
    print("Opçao invalida de pagamento: ")