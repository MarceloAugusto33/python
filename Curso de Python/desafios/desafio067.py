while True:
    tabuada = float(input("Digite um numero para ver sua tabuada: "))
    if tabuada < 0:
        print("Programa Finalizado!")
        break
    contador = 1
    while contador <= 10:
        print(f"{tabuada:.0f} x {contador} = {tabuada*contador:.0f}")
        contador +=1