def abelha_maja(x, y, v, n):
    if n == 1:
        return x, y, v, n
    while True:
        v += 1
        y += 1
        n -= 1
        if n == 1:
            return x, y, v, n

        for i in range(v - 1):
            x -= 1
            y += 1
            n -= 1
            if n == 1:
                return x, y, v, n

        for i in range(v):
            x -= 1
            n -= 1
            if n == 1:
                return x, y, v, n

        for i in range(v):
            y -= 1
            n -= 1
            if n == 1:
                return x, y, v, n

        for i in range(v):
            x += 1
            y -= 1
            n -= 1
            if n == 1:
                return x, y, v, n

        for i in range(v):
            x += 1
            n -= 1
            if n == 1:
                return x, y, v, n

        for i in range(v):
            y += 1
            n -= 1
            if n == 1:
                return x, y, v, n
while True:
    try:
        n = int(input())
        x = y = v = 0
        x,y,v,n = abelha_maja(x,y,v,n)
        print(x, y)
    except EOFError:
        break