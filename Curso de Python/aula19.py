def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(f"A {lst} tem {len(lst)} valores")
valores = [7,2,5,0,4]
dobra(valores)
print(valores)