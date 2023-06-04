Dinheiro=float(input())

Notas = Dinheiro
Nota100 = Notas/100
resto = Notas%100
Nota50 = resto/50
resto = resto%50
Nota20 = resto/20
resto = resto%20
Nota10 = resto/10
resto = resto%10
Nota5 = resto/5
resto = resto%5
Nota2 = resto/2
Moeda1 = resto%2

Moedas = int(Dinheiro*100)
resto = Moedas%100
Moeda050 = resto/50
resto = resto%50
Moeda025 = resto/25
resto = resto%25
Moeda010 = resto/10
resto = resto%10
Moeda005 = resto/5
Moeda001 = resto%5

print("NOTAS:")
print(f"{int(Nota100)} nota(s) de R$ 100.00")
print(f"{int(Nota50)} nota(s) de R$ 50.00")
print(f"{int(Nota20)} nota(s) de R$ 20.00")
print(f"{int(Nota10)} nota(s) de R$ 10.00")
print(f"{int(Nota5)} nota(s) de R$ 5.00")
print(f"{int(Nota2)} nota(s) de R$ 2.00")
print(f"MOEDAS:")
print(f"{int(Moeda1)} moeda(s) de R$ 1.00")
print(f"{int(Moeda050)} moeda(s) de R$ 0.50")
print(f"{int(Moeda025)} moeda(s) de R$ 0.25")
print(f"{int(Moeda010)} moeda(s) de R$ 0.10")
print(f"{int(Moeda005)} moeda(s) de R$ 0.05")
print(f"{int(Moeda001)} moeda(s) de R$ 0.01")