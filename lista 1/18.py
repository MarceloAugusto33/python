MB = int(input("Qual tamanho do arquivo: "))
mbps = int(input("Qual velocidade da sua internet: "))
t = MB/mbps
tm = t/60
tm = round(tm, 2)
print(str(tm)+" minuto")
print("Lista terminada em 50 minutos!!!!")