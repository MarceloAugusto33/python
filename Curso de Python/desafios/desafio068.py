from random import randint
print("="*20)
print("Jogo Par ou Impar")
print("="*20)
ganho = 0
while True:
    comp = randint(1,10)
    n = int(input("Digite um numero: "))
    op = input("Par ou Impar : [P]/[I]: ").strip()[0]
    while op not in "Pp" and op not in "Ii":
        print("Comando Invalido!")
        print("Somente [P] ou [I]")
        op = input("Par ou Impar : [P]/[I]: ").strip()[0]
    print("-"*30)
    numero = n + comp
    if op in "Pp":
        if numero % 2 == 0:
            print("-"*30)
            print(f"Voce jogou o numero {n} e a maquina jogou {comp} a soma deu {numero}")
            print("-"*30)
            ganho +=1
            print("\033[42mVoce Venceu Vamos jogar Novamente...\033[m")
            print("-"*30)
        else:
            print("-"*30)
            print("\033[41mGamer Over!\033[m Voce Perdeu") 
            break
    elif op in "Ii":
        if numero % 2 != 0:
            print("-"*30)
            print(f"Voce jogou o numero {n} e a maquina jogou {comp} a soma deu {numero}")
            print("-"*30)
            ganho +=1
            print("\033[42mVoce Venceu Vamos jogar Novamente...\033[m")
            print("-"*30)
        else:
            print("-"*30)
            print("\033[41mGamer over!\033[m Voce Perdeu")
            break
print("-"*30)
print(f"Voce jogou o numero {n} e a maquina jogou {comp} a soma deu {numero}")
print(f"Quantida de vitorias: {ganho}")
print("-"*30)



