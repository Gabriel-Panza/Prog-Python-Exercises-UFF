qntd_de_palavras = int(input())

for i in range(qntd_de_palavras):
    palavra = input()
    qntd_que_avanca = int(input())
    palavra_decodificada = ""
    for j in palavra:
        letra = ord(j)-qntd_que_avanca
        if letra < 65:
            palavra_decodificada += chr(91-(65-letra))
        else:
            palavra_decodificada += chr(letra)
    print(palavra_decodificada)