N_testes = int(input())
teste = 0

while N_testes > 0:
    x = -10000
    y = 10000
    u = 10000
    v = -10000

    for i in range(N_testes):
        a, b, c, d = map(int, input().split())
        if a > x:
            x = a
        if b < y:
            y = b
        if c < u:
            u = c
        if d > v:
            v = d

    teste += 1
    print(f"Teste {teste}")
    if x < u and v < y:
        print(f"{x} {y} {u} {v}", end="\n\n")
    else:
        print("nenhum", end="\n\n")

    N_testes = int(input())
