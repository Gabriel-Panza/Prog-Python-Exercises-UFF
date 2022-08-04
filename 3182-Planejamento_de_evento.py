precoQUartos = []
quartos = []
quarto = False
participantes, orcamento, QntdHotel, QntdSemanas = map(int, input().split())

for i in range(QntdHotel):
    precoPer = int(input())
    intNCamas = list(map(int, input().split()))
    precoTotal = participantes * precoPer
    for k in intNCamas:
        if participantes <= k and precoTotal <= orcamento:
            quartos.append(precoTotal)
            set(quartos)
            quarto = True
menor_preco = 500000
for g in quartos:
    if g < menor_preco:
        menor_preco = g
if quarto:
    print(menor_preco)
else:
    print("stay home")
