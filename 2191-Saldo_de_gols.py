def compare(maior, saldo, ini, fim):
    sizeM = maior[2] - maior[1]
    size = fim - ini
    if saldo > maior[0]:
        maior = [saldo, ini, fim]
    elif saldo == maior[0] and size > sizeM:
        maior = [saldo, ini, fim]
    return maior


def main():
    n = int(input())
    case = 0
    while n != 0:
        lista = [None]
        valor = -51
        ini, fim = 1, 1
        maior = [valor, 1, 1]
        while n != 0:
            jogo = list(map(int, input().split()))
            saldo = jogo[0] - jogo[1]
            result = saldo + valor
            indice = len(lista)
            if saldo > result:
                if saldo > valor:
                    valor = saldo
                    ini = indice
                    fim = indice
            else:
                if valor <= result:
                    valor = result
                    fim = indice
                else:
                    fim = indice - 1
                    valor = result
            maior = compare(maior, valor, ini, fim)
            lista.append(saldo)
            n -= 1
        case += 1
        print(f"Teste {case}")
        if maior[0] <= 0:
            print("nenhum", end="\n\n")
        else:
            print(maior[1], maior[2], end="\n\n")
        n = int(input())

main()