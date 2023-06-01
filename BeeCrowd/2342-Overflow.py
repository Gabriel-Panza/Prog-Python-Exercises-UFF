maximo = int(input())
operacao = input().split()
numero1 = int(operacao[0])
numero2 = int(operacao[2])
if operacao[1] == '+':
    resultado = numero1 + numero2
    if resultado <= maximo:
        print("OK")
    else:
        print("OVERFLOW")
elif operacao[1] == '*':
    resultado = numero1 * numero2
    if resultado <= maximo:
        print("OK")
    else:
        print("OVERFLOW")