frase = str(input("Digite uma frase: ")).strip().lower()
print("A letra 'A' apareceu {} vezes".format(frase.count("a")))
print("A letra A aparece na posiçao {}".format(frase.find("a")+1))
print("Ela aparece pela ultima vez na posiçao {}".format(frase.rfind("a")+1))
