import collections

error, value = map(int, input().split())
emptyList = []
while error!= 0 and value != 0:
    error = str(error)
    value = str(value)
    for i in range(len(str(error))):
        value = value.replace(error[i],"")
    lista_com_zeros = ["0"] * len(value)
    if collections.Counter(value) != collections.Counter(emptyList) and collections.Counter(value) != collections.Counter(lista_com_zeros):
        print(int(value))
    else:
        print(0)
    error, value = map(int, input().split())