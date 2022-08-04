mensagem_criptograda=input()
codigo=input()
possibilidadesDeCodigo=0

for i in range(len(mensagem_criptograda)-len(codigo)+1):
    pos=0
    verificador=0
    for j in range(i, i+len(codigo)):
        if mensagem_criptograda[j]==codigo[pos]:
            verificador+=1
            break
        pos+=1
    if verificador==0:
        possibilidadesDeCodigo+=1
print(possibilidadesDeCodigo)