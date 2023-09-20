inteiro = int(input("Escolha um numero inteiro: "))
print('''Escolha uma opçao
[ 1 ] binario
[ 2 ] octal
[ 3 ] hexadecimal''')
escolha = int(input("Digite uma opçao: "))
if escolha == 1:
    print("Binario: {}".format(bin(inteiro)[2:]))
elif escolha == 2:
    print("Octal: {}".format(oct(inteiro)[2:]))
elif escolha == 3:
    print("hexadecimaç: {}".format(hex(inteiro)[2:]))
else:
    print("\033[41mopçao invalida\033[m")
