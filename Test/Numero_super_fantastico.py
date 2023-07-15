def eh_primo(numero):
    if numero < 2:
        return False

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def verifica_digitos_primos(numero):
    for digito in str(numero):
        if not eh_primo(int(digito)):
            return False
    return True

while True:
    numero = int(input())  # Número a ser verificado
    if numero == 0:
        break

    # Verifica se o número é primo e se seus dígitos também são primos
    if eh_primo(numero) and verifica_digitos_primos(numero):
        print("Super")
    else:
        print("Normal")