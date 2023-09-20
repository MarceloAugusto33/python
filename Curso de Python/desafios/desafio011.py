largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))
area = largura*altura
litros_tinta = area/2
print("Voce precisa de {:.2f} litros de tinta para pintar toda a parede de area {}".format(litros_tinta,area))