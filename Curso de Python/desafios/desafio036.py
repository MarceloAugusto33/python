valor_casa = float(input("Informe o valor da casa: "))
salario_comprador = float(input("Digite o Seu salario: "))
anos = int(input("Em quantos anos voce pretende pagar: "))
ano = 12
meses_totais = ano*anos
valor_prestacao = valor_casa / meses_totais
if valor_prestacao > (salario_comprador*(30/100)):
    print("-=-"*20)
    print("\033[41mImprestimo negado!\033[m \nO Valor da prestaçao ficará mais de 30%' do seu salario")
    print("O valor da casa foi de: {}\nO seu salario é de: {}\nAnos de prestaçao: {}\nValor de cada prestaçao: R${:.2f}".format(valor_casa,salario_comprador,anos,valor_prestacao))
    print("-=-"*20)
else:
    print("-=-"*20)
    print("\033[42mEmprestimo Aprovado!\033[m")
    print("O valor da casa foi de: {}\nO seu salario é de: {}\nAnos de prestaçao: {}\nValor de cada prestaçao: R${:.2f}".format(valor_casa,salario_comprador,anos,valor_prestacao))
    print("-=-"*20)

