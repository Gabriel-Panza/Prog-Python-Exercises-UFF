N = int(input())                            # indica o número de trilhas
D = []                                      # diferenças de altura final de cada trilha 
menor = 100000 
for i in range(1,N+1):
    indice = input()                        # qntd de alturas
    M = int(indice.split()[0])              # separo a qntd de alturas das alturas em si
    lista = list(map(int, indice.split()))  # lista de alturas por ponto de medição
    t_subida = 0
    t_descida = 0
    
    for j in range(0,len(lista)-1):
        trilha = lista[j+1] - lista[j]      # qntd de esforço até a proxima altura
        if trilha > 0:                      # se o esforço for positivo
            t_subida += trilha              # adicione o esforço na trilha da subida
        if trilha < 0:                      # se o esforço for negativo
            t_descida += trilha             # adicione o esforço na trilha da descida
    t_descida *= -1                         # Como a descida deu esforço negativo, multiplico por -1 para fins de comparação com a subida
    if t_subida < t_descida :               # Se a ida for o caminho mais curto, escolho ela
        D.append(t_subida)
    else:                                   # Se a volta for o caminho mais curto, escolho ela
        D.append(t_descida)
        
for y in range(0, len(D)):                  # Percorro a lista de esforço
   if D[y] < menor :                        # Se o termo de posição y da lista for menor que o menor numero
       menor = D[y]                         # ele se torna o menor
       melhor_trilha = y + 1                # E salva-se o indice da trilha em uma variável (soma-se +1, pq o loop começa no 0)
print(melhor_trilha)