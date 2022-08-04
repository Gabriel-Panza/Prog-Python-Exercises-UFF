Mx, My, Rx, Ry = map(int, input().split())
coordenada_x = Rx - Mx
coordenada_y = Ry - My
cruzamentos = abs(coordenada_x) + abs(coordenada_y)
print(cruzamentos)