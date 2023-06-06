# Criando uma lista
lista1 = []
print(lista1)
lista2 = []*10
print(lista2)
lista3 = [0]
print(lista3)
lista4 = [0]*10
print(lista4)


print("\n\n")
# Adicionando elementos em uma lista vazia
lista = []
for index in range(3):
    elementoString = input("Digite o seu nome: ")
    lista.append(elementoString)
print(lista)

lista = []
for index in range(3):
    lista.append(input("Digite o seu nome: "))
print(lista)


print("\n\n")
# Substituindo elementos de uma lista pre-criada
lista = [0]*3
print(lista)
for index in range(3):
    lista[index] = input("Digite o seu nome: ")
print(lista)

lista[0] = input("Digite outro nome: ")
print(lista)


print("\n\n")
# Removendo elementos
lista = [1, 2, 3, 4, "Pedro", 6, "Gabriel", 8, 9, 10]
lista.remove("Gabriel")
lista.remove("Pedro")
print(lista)

lista = [1, 2, 3, 4, "Pedro", 6, "Gabriel", 8, 9, 10]
lista.pop(6)
lista.pop(4)
print(lista)

lista.clear()
print(lista)


print("\n\n")
# Percorrendo uma lista
lista = [1, 2, 3, 4, "Pedro", 6, "Gabriel", 8, 9, 10]
for index in range(len(lista)):
    print(lista[index])
    
for elemento in lista:
    print(elemento)