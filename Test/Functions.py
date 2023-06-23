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
    return a/b

print("Add: ", add(4,6))
print("Sub: ", sub(10,5))
print("Mult: ", mult(2,5))
print("Div: ", div(6,3))
print("Comparando a soma e a divisao, temos que o maior é:", compare(add(4,6),div(6,3)))
print("Comparando numeros...S", compare(compare(add(1,2),mult(1,2)),compare(sub(5,2),div(6,1))))
