palavra_codificada = input()
texto_sem_sentido = input()
palavra_decifrada = []
alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]
for i in texto_sem_sentido:
    cont = 0
    for j in palavra_codificada:
        if i == j:
            palavra_decifrada.append(alfabeto[cont])
        cont += 1
print("".join(palavra_decifrada))