import math
angulo = int(input("Digite um angulo: "))
cos = math.cos(math.radians(angulo))
sen = math.sin(math.radians(angulo))
tanj = math.tan(math.radians(angulo))
print("O angulo de {} tem cos{:.2f} sen{:.2f} tan{:.2f}".format(angulo,cos,sen,tanj))