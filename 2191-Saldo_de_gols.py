def compare(higher, saldo, start, end):
    sizeM = higher[2] - higher[1]
    size = end - start
    if saldo > higher[0]:
        higher = [saldo, start, end]
    elif saldo == higher[0] and size > sizeM:
        higher = [saldo, start, end]
    return higher


def main():
    n = int(input())
    case = 0
    while n != 0:
        list = [None]
        value = -51
        start, end = 1, 1
        higher = [value, 1, 1]
        while n != 0:
            game = list(map(int, input().split()))
            saldo = game[0] - game[1]
            result = saldo + value
            index = len(list)
            if saldo > result:
                if saldo > value:
                    value = saldo
                    start = index
                    end = index
            else:
                if value <= result:
                    value = result
                    end = index
                else:
                    end = index - 1
                    value = result
            higher = compare(higher, value, start, end)
            list.append(saldo)
            n -= 1
        case += 1
        print(f"Test {case}")
        if higher[0] <= 0:
            print("none", end="\n\n")
        else:
            print(higher[1], higher[2], end="\n\n")
        n = int(input())

main()