N_tests = int(input())
test = 0

while N_tests > 0:
    x = -10000
    y = 10000
    u = 10000
    v = -10000

    for i in range(N_tests):
        a, b, c, d = map(int, input().split())
        if a > x:
            x = a
        if b < y:
            y = b
        if c < u:
            u = c
        if d > v:
            v = d

    test += 1
    print(f"Test {test}")
    if x < u and v < y:
        print(f"{x} {y} {u} {v}", end="\n\n")
    else:
        print("none", end="\n\n")

    N_tests = int(input())
