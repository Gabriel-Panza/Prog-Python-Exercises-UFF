import collections

erro, valor = map(int, input().split())
lista_vazia = []
while erro!= 0 and valor != 0:
    erro = str(erro)
    valor = str(valor)
    for i in range(len(str(erro))):
        valor = valor.replace(erro[i],"")
    lista_com_zeros = ["0"] * len(valor)
    if collections.Counter(valor) != collections.Counter(lista_vazia) and collections.Counter(valor) != collections.Counter(lista_com_zeros):
        print(int(valor))
    else:
        print(0)
    erro, valor = map(int, input().split())