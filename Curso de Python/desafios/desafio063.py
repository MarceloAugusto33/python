print("Sequencia de fibonacci!")
termos = int(input("Quantos termos:  "))
t1 = 0
t2 = 1
contador = 0
while contador <= termos:
    print("{} ".format(t1),end=" ")
    prx = t1 + t2
    t1 = t2
    t2 = prx
    contador +=1
