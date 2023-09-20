ext = ("zero","um","dois","tres","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quatorze","quinze","dezesseis","dezessete","desoito","dezenove","vinte")
n = int(input("Escolha um numero de 0 a 20: "))
while n < 0 or n > 20:
    n = int(input("Tente nvamente!Escolha um numero de 0 a 20: "))
print(f"Voce digitou o numero {ext[n]}")
