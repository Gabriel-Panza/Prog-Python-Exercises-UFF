a, b, c, d = map(int, input().split())

if b == d:
    numerador = a+c
    divisor = b
else:
    mdc = b*d
    x = int(mdc/b) * a
    y = int(mdc/d) * c
    numerador = x+y
    divisor = mdc

for i in range(2,101):
    while numerador%i==0 and divisor%i==0:
        numerador = int(numerador/i)
        divisor = int(divisor/i)
print(numerador, divisor)