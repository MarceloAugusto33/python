reta1 = int(input("digite o 1 valor para a reta: "))
reta2 = int(input("Digite o 2 valor para a reta: "))
reta3 = int(input("Digite o 3 valor para reta: "))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("Essas retas formam um triangulo!")
else:
    print( "Nao forma um triangulo!")

