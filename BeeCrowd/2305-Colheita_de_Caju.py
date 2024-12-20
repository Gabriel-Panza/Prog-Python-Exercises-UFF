# Recebendo os dados de linhas e colunas
linhas_plantacao, colunas_plantacao, linhas_lote, colunas_lote = map(int,input().split())

# Criando a matriz da plantacao
plantacao = []
for i in range(linhas_plantacao):
    plantacao.append(list(map(int,input().split())))

# Criando a matriz de somas parciais
somas_parciais = []
for _ in range(linhas_plantacao + 1):
    somas_parciais.append([0] * (colunas_plantacao + 1))

# Pré-cálculo das somas parciais
for i in range(1, linhas_plantacao + 1):
    for j in range(1, colunas_plantacao + 1):
        somas_parciais[i][j] = (plantacao[i-1][j-1] 
                                + somas_parciais[i-1][j] 
                                + somas_parciais[i][j-1] 
                                - somas_parciais[i-1][j-1])

somas = 0
for linhas in range(linhas_plantacao + 1 - linhas_lote):
    for colunas in range(colunas_plantacao + 1 - colunas_lote):
        cajus = (somas_parciais[linhas + linhas_lote][colunas + colunas_lote] 
                - somas_parciais[linhas][colunas + colunas_lote] 
                - somas_parciais[linhas + linhas_lote][colunas] 
                + somas_parciais[linhas][colunas])
        
        if cajus > somas:
            somas = cajus

print(somas)