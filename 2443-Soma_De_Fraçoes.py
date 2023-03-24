a, b, c, d = map(int, input().split())

if b == d:
    number = a+c
    div = b
else:
    mdc = b*d
    x = int(mdc/b) * a
    y = int(mdc/d) * c
    number = x+y
    div = mdc

for i in range(2,101):
    while number%i==0 and div%i==0:
        number = int(number/i)
        div = int(div/i)
print(number, div)