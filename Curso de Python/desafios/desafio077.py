tupla = ("Marcelo","Renan","Augusto","Tavares","Inacio","Gomes")
vogal = ""
for c in tupla:
    vogal = ""
    for p in c:
        if p in "aAeEIiOoUu":
            vogal += p
    print(f"A palavra {c} tem as vogais: {' '.join(vogal)}")    
