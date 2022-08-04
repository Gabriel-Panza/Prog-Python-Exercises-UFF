qntd_de_testes = int(input())
for i in range(qntd_de_testes):
    x1,y1,x2,y2,x3,y3 = map(int, input().split())
    area = ((x1*y2 + x2*y3 + x3*y1) - (y1*x2 + y2*x3 + y3*x1)) / 2
    if area < 0:
        area *= -1
    print("%.3f"%area)