import time
def contador(i,f,p):
    cont = i
    if f > i and p > 0:
        while cont <= f:
            print(f"{cont} ")
            cont += p
            time.sleep(0.5)
        print("="*30)
    else:
        while cont >= f or p == 0:
            print(f"{cont} ")
            cont -= p
            time.sleep(0.5)
        print("="*30)
contador(1,10,1)
contador(10,0,2)
inicio = int(input("Qual numero voce quer começar: "))
fim = int(input("QUal numero voce quer terminar: "))
passo = int(input("De quanto em quanto voce quer contar: "))
contador(inicio,fim,passo)