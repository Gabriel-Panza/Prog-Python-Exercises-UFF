P1 = float(input("P1: "))
Seminario = float(input("Seminario: "))
Trabalho = float(input("Trabalho: "))
Media = float(input("Quanto de media vc quer ter no final: "))

MediaSemP2 = ((P1 * 0.7 + Seminario * 0.3) + Trabalho)

P2 = (Media*3)-(MediaSemP2)

if (P2<=10):
    print("Vc precisa tirar na P2 para alcançar média final %d: ", Media)
    print(f'{P2:.2f}')
else:
    print("Vc não consegue alcançar essa média final com as notas tiradas!")