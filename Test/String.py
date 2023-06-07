# Criando uma string
palavra = input("Escreva uma palavra: ")
print(palavra)
frase = input("Escreva uma frase: ")
print(frase)

print("\n\n")
# Funções importantes
frase_sem_espacos_inicioFim = frase.strip()
print(frase_sem_espacos_inicioFim)
frase_sem_virgula = frase.replace(',', ' ')
print(frase_sem_virgula)
frase_quebrada = frase.split(',')
print(frase_quebrada)

print()

palavra_upper = palavra.upper()
print(palavra_upper)
palavra_lower = palavra.lower()
print(palavra_lower)
index_letra = palavra.find("i")
print(index_letra)
index_letra = palavra.find("y")
print(index_letra)

print("\n\n")
# Percorrendo
for index in range(len(palavra)):
    print(palavra[index])
print()
for letra in palavra:
    print(letra)