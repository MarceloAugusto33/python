reta1 = int(input("digite o 1 valor para a reta: "))
reta2 = int(input("Digite o 2 valor para a reta: "))
reta3 = int(input("Digite o 3 valor para reta: "))

if reta1 < reta2+reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("Pode sim formar um triangulo")
    if reta1 == reta2 and reta2 == reta3:
        print("Vai formar um triangulo Equilatero!")
    elif reta1 == reta2 and reta2 != reta3 or reta2 == reta3 and reta3 != reta1 or reta1 == reta3 and reta3 != reta2:
        print("Vai formar um triangulo Isoceles, dois lados iguais,um diferente")
    elif reta1 != reta2 and reta2 != reta3:
        print("Triangulo escaleno, todos os lados diferentes")
else:
    print("Nao pode formar um triangulo!")
