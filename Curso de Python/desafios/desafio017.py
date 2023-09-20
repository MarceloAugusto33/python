from math import hypot
Cateto_oposto = float(input("Digite o cateto oposto da hipotenusa: "))
Cateto_adjacente = float(input("Digite o cateto adjacente da hipotenusa: "))
hipotenusa = hypot(Cateto_adjacente,Cateto_oposto)
print("O comprimento da hipotenusa de catetos equivalentes {} e {} vale {:.2f}".format(Cateto_oposto,Cateto_adjacente,hipotenusa))
