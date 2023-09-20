from time import sleep
n1 = int(input("Digite um numero: "))
n2 = int(input("digite outro  numero: "))
opcao = 0
while opcao != 5:
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos numeros')
    print('[ 5 ] Sair do programa')
    opcao = int(input("Digite uma opcao acima: "))
    while opcao < 1 or opcao > 5:
        print("Comando invalido Tente novamente!")
        opcao = int(input("Digite uma opcao acima: "))
    if opcao == 1:
        soma = n1 + n2
        print("A soma {} + {} = {}".format(n1,n2,n1+n2))
    elif opcao == 2:
        multiplicar = n1 * n2
        print("A Multiplicaçao {} x {} = {}".format(n1,n2,n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            print("O maior numero é o {}".format(n1))
        else:
            print("O maior numeor é o {}".format(n2))
    elif opcao == 4:
        n1 = int(input("Digite um numero: "))
        n2 = int(input("digite outro  numero: "))
    elif opcao == 5:
        print("Saindo do programa...")
        sleep(2)
        print("...")
        sleep(2)
print("Programa finalizado")