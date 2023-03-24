def CreateTemp(temperature):
    for k in range(N_Temperatures):
        temperature.append(int(input()))
        
def AdditionTemp(temperatura,somas,soma):
    for j in range(M_intervals):
        soma += temperatura[j]
    somas.append(soma)
    for i in range(N_Temperatures-M_intervals):
        soma += temperatura[i+M_intervals] - temperatura[i]
        somas.append(soma)
        
def SetBiggerLower(bigger,lower,adds):
    for l in adds:
        if l > bigger:
            bigger = l
        if l < lower:
            lower = l    
    list_lowers_biggers.append(int(lower/M_intervals))
    list_lowers_biggers.append(int(bigger/M_intervals))    
        

list_lowers_biggers = []
cont=1
N_Temperatures, M_intervals = map(int, input().split())
while N_Temperatures!=0 and M_intervals!=0:
    temperature = []
    adds = []
    add = 0
    bigger = -201
    lower = 201
    
    CreateTemp(temperature)
    AdditionTemp(temperature,adds,add)    
    SetBiggerLower(bigger,lower,adds)
    
    N_Temperatures, M_intervals = map(int, input().split())

for i in range(0,len(list_lowers_biggers),2):
    print("Test {}".format(cont))
    print(list_lowers_biggers[i], list_lowers_biggers[i+1])
    print()
    cont+=1