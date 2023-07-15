def determinar_vencedor(partidas):
    vencedores = []
    
    for partida in partidas:
        a, b = partida
        soma = a + b
        
        if soma % 2 == 0:
            vencedores.append(jogador1)
        else:
            vencedores.append(jogador2)
    
    return vencedores

# Leitura da entrada
numero_teste = 1
while True:
    n = int(input())  # Número de partidas
    if n == 0:
        break
    
    jogador1 = input()  # Nome do jogador 1
    jogador2 = input()  # Nome do jogador 2
    
    partidas = []
    for _ in range(n):
        a, b = map(int, input().split())  # Números de dedos mostrados por cada jogador
        partidas.append((a, b))
    
    # Determinar o vencedor de cada partida
    vencedores = determinar_vencedor(partidas)
    
    # Imprimir o resultado
    print(f"Teste {numero_teste}")
    for vencedor in vencedores:
        print(vencedor)
    print()
    
    numero_teste += 1