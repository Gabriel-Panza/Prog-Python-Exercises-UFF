def CriaTemp(temperatura):
    for k in range(N_Temperaturas):
        temperatura.append(int(input()))
        
def SomaDeTemperaturas(temperatura,somas,soma):
    for j in range(M_intervalos):
        soma += temperatura[j]
    somas.append(soma)
    for i in range(N_Temperaturas-M_intervalos):
        soma += temperatura[i+M_intervalos] - temperatura[i]
        somas.append(soma)
        
def DefineMaiorMenor(maior,menor,somas):
    for l in somas:
        if l > maior:
            maior = l
        if l < menor:
            menor = l    
    # Salvo os maiores e menores
    lista_menores_maiores.append(int(menor/M_intervalos))
    lista_menores_maiores.append(int(maior/M_intervalos))    
        

lista_menores_maiores = []
cont=1
N_Temperaturas, M_intervalos = map(int, input().split())
while N_Temperaturas!=0 and M_intervalos!=0:
    temperatura = []
    somas= []
    soma=0
    maior= -201
    menor = 201
    
    # Chamo as funçoes
    CriaTemp(temperatura)
    SomaDeTemperaturas(temperatura,somas,soma)    
    DefineMaiorMenor(maior,menor,somas)
    
    # Repito o loop
    N_Temperaturas, M_intervalos = map(int, input().split())

for i in range(0,len(lista_menores_maiores),2):
    print("Teste {}".format(cont))
    print(lista_menores_maiores[i], lista_menores_maiores[i+1])
    print()
    cont+=1