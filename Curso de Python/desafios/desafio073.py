serieA = ("Botafogo","Palmeiras","Flamengo","Atletico-MG","Fluminense","Gremio","atletico-PR","Sao paulo","Cruzeiro","Internacional","Fortaleza","Bragantino","Santos","Cuiaba","Bahia","Corinthians","Goias","America-MG","Vasco da Gama","Coritiba")
print(f"Os 5 primeiros colocados: {serieA[:5]}")
print("="*30)
print(f"Os 4 ultimos da  tabela: {serieA[16:]}")
print("="*30)
print(f"Lista dos times em ordem alfabetica: {sorted(serieA)}")
print("="*30)
bahia = "Bahia"
print(f"Bahia está na posiçao {serieA.index(bahia)+1}")