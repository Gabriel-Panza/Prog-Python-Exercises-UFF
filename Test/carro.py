lista_carros = []

N = int(input("Informe quantos carros tem: "))
for i in range(N):
    carro = input("Informe o modelo do carro: ")
    rendimento = float(input("Informe o rendimento do carro: "))
    lista_carros.append([carro,rendimento])
    # carro, rendimento = map(str, input("Informe o modelo e rendimento do carro\n").split(" "))
    # lista_carros.append([carro,float(rendimento)])

lista_custos = []
carro_economico = lista_carros[0][0]
rendimento_economico = lista_carros[0][1]
for index in range(len(lista_carros)):
    custo = (1000 / lista_carros[index][1]) * 3.5
    lista_custos.append(custo)
    if (lista_carros[index][1] > rendimento):
        carro_economico = lista_carros[index][0]

print(*lista_custos)
print(f"O carro mais economico é: {carro_economico}")