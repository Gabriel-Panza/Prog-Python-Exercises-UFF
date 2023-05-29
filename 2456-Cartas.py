n = list(map(int,input().split()))
if n[0] > n[1] > n[2] > n[3] > n[4]:
    print('D')
elif n[0] < n[1] < n[2] < n[3] < n[4]:
    print('C')
else:
    print('N')