lista = [1,2,3,4,5,6,7,8,9,10] -1
for i in range(0,len(lista)): 
    print(lista[i])
print("\n\n")

for i in range(1,len(lista)+1):
    print(lista[-i])
print("\n\n")

for i in range(len(lista)-1,-1,-1):
    print(lista[i])
print("\n\n")

for i in range(len(lista),0,-1):  # onde o for para = stop - step
    print(lista[-i])