galera = []
todos = []
for c in range(0,2):
    galera.append(input("Nome: "))
    galera.append(int(input("idade: ")))
    todos.append(galera[:])
    galera.clear()
print(todos)