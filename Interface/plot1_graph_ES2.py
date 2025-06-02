import matplotlib.pyplot as plt
import numpy as np

# Definição dos parâmetros do gráfico (inalterados)
orcamento_max = 43650.00
semanas_max = 14
semana_parada_ev_ac = 5
ev_na_semana_parada = 12981.51
ac_na_semana_parada = 5950.00

# 1. PV (Valor Planejado) - MODIFICADO (mantido como no passo anterior)
x_pv = np.array(range(semanas_max + 1))
y_pv = np.zeros(semanas_max + 1)

# Segmento 1 do PV
if semana_parada_ev_ac > 0:
    slope_pv1 = ev_na_semana_parada / semana_parada_ev_ac
    for i in range(semana_parada_ev_ac + 1):
        y_pv[i] = i * slope_pv1
    y_pv[semana_parada_ev_ac] = ev_na_semana_parada
elif semana_parada_ev_ac == 0:
    y_pv[0] = ev_na_semana_parada

# Segmento 2 do PV
ponto_inicial_pv2_x = semana_parada_ev_ac
ponto_inicial_pv2_y = ev_na_semana_parada
ponto_final_pv2_x = semanas_max
ponto_final_pv2_y = orcamento_max

if ponto_final_pv2_x > ponto_inicial_pv2_x:
    slope_pv2 = (ponto_final_pv2_y - ponto_inicial_pv2_y) / (ponto_final_pv2_x - ponto_inicial_pv2_x)
    for i in range(ponto_inicial_pv2_x + 1, ponto_final_pv2_x + 1):
        y_pv[i] = ponto_inicial_pv2_y + (i - ponto_inicial_pv2_x) * slope_pv2
    y_pv[ponto_final_pv2_x] = ponto_final_pv2_y

# 2. EV (Valor Agregado) - Inalterado
x_ev = np.array(range(semana_parada_ev_ac + 1))
y_ev = np.zeros(semana_parada_ev_ac + 1)
if semana_parada_ev_ac > 0:
    slope_ev = ev_na_semana_parada / semana_parada_ev_ac
    for i in range(1, semana_parada_ev_ac + 1):
        y_ev[i] = i * slope_ev
    y_ev[semana_parada_ev_ac] = ev_na_semana_parada
elif semana_parada_ev_ac == 0:
    if len(y_ev) > 0:
         y_ev[0] = ev_na_semana_parada

# 3. AC (Custo Real) - Inalterado
x_ac = np.array(range(semana_parada_ev_ac + 1))
y_ac = np.zeros(semana_parada_ev_ac + 1)
if semana_parada_ev_ac > 0:
    slope_ac = ac_na_semana_parada / semana_parada_ev_ac
    for i in range(1, semana_parada_ev_ac + 1):
        y_ac[i] = i * slope_ac
    y_ac[semana_parada_ev_ac] = ac_na_semana_parada
elif semana_parada_ev_ac == 0:
     if len(y_ac) > 0:
        y_ac[0] = ac_na_semana_parada

# Criação do Gráfico
# Alteração aqui: figsize=(12, 6) para "achatar" o eixo Y visualmente
plt.figure(figsize=(12, 6))

plt.plot(x_pv, y_pv, label='PV (Valor Planejado)', marker='.', linestyle='-', color='blue')
plt.plot(x_ev, y_ev, label='EV (Valor Agregado)', marker='.', linestyle='-', color='green')
plt.plot(x_ac, y_ac, label='AC (Custo Real)', marker='.', linestyle='-', color='red')

# Configurações do Gráfico
plt.title('Gráfico de Valor Agregado - Aé 04/05/2025', fontsize=16)
plt.xlabel('Semanas', fontsize=14)
plt.ylabel('Custo (R$)', fontsize=14)

plt.xlim(0, semanas_max)
plt.ylim(0, orcamento_max * 1.05)

plt.xticks(np.arange(0, semanas_max + 1, 1))
plt.yticks(np.arange(0, orcamento_max + 5000, 5000))

plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# Salvar e mostrar o gráfico
plt.savefig('grafico_valor_agregado_pv_ajustado_achatado.png')
plt.show()