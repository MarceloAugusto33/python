from time import sleep
def maior(*n):
    maior = n[0]
    print("Analisando valores passados: ")
    for valor in n:
        print(f"{valor}")
        if valor > maior:
            maior = valor
        sleep(0.5)
    print(f"\nO maior valor da lista {n} é o {maior}")
maior(2,9,4,5,7,1)

