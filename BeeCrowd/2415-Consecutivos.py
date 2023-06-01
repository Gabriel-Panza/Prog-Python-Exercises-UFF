N_qnt_numbers = int(input())
N_numbers = list(map(int, input().split()))
BiggerSequencial=[]
cont=1
for i in range(N_qnt_numbers-1):
    if N_numbers[i]==N_numbers[i+1]:
        cont+=1
    else:
        BiggerSequencial.append(cont)
        cont=1
BiggerSequencial.append(cont)
BiggerSequencial.sort()
print(BiggerSequencial[-1])