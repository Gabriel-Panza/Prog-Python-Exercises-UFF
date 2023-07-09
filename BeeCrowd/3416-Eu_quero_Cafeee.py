alunos, ltsporvez, mlsporaluno = map(int,input().split()) #sai em ml
ltsporaluno = mlsporaluno / 1000 #em litros
total = ltsporaluno * alunos
if total <= ltsporvez:
    print(ltsporvez)
else:
    if total % ltsporvez == 0:
        vezesmaior = total / ltsporvez
    else:
        vezesmaior = total // ltsporvez + 1
    print(f"{ltsporvez * vezesmaior:.0f}")