def compare(a,b):
    if(a>b):
        return a 
    return b

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a%b

a = add(4,6)
s = sub(10,5)
m = mult(2,5)
d = div(6,3)
print(a)
print(s)
print(m)
print(d)
print("Comparando a soma:", a, " e a divisao:", d, " temos que o maior é:", compare(a,d))