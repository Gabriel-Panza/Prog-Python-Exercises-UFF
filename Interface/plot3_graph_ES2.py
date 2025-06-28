import matplotlib.pyplot as plt
import numpy as np

# --- Parâmetros Globais do Projeto ---
orcamento_max = 43650.00
semanas_max = 14

# --- Parâmetros que definem a forma da curva PV (Inalterado) ---
semana_parada_ev_ac_para_pv = 5
ev_na_semana_parada_para_pv = 12981.51

# --- Parâmetros históricos para EV e AC ---
ev_valor_semana5 = 12981.51
ev_valor_semana9 = 24941.61

ac_valor_semana5 = 5950.00
ac_valor_semana9 = 23625.00

# --- Parâmetros Finais do Projeto (Semana 14) ---
ev_valor_final = 43650.00
ac_valor_final = 35125.00

# --- Prazos para as novas fases de crescimento ---
semana_pausa_fim = 12.5
semana_crescimento_rapido_fim = 13.5

# --- 1. PV (Valor Planejado)
x_pv = np.array(range(semanas_max + 1))
y_pv = np.zeros(semanas_max + 1)
# (O restante do bloco do PV é idêntico ao código anterior, resultando na mesma curva)
# Segmento 1 do PV
if semana_parada_ev_ac_para_pv > 0:
    slope_pv1 = ev_na_semana_parada_para_pv / semana_parada_ev_ac_para_pv
    for i in range(semana_parada_ev_ac_para_pv + 1):
        y_pv[i] = i * slope_pv1
    y_pv[semana_parada_ev_ac_para_pv] = ev_na_semana_parada_para_pv
elif semana_parada_ev_ac_para_pv == 0:
    y_pv[0] = ev_na_semana_parada_para_pv
# Segmento 2 do PV
ponto_inicial_pv2_x = semana_parada_ev_ac_para_pv
ponto_inicial_pv2_y = ev_na_semana_parada_para_pv
ponto_final_pv2_x = semanas_max
ponto_final_pv2_y = orcamento_max
if ponto_final_pv2_x > ponto_inicial_pv2_x:
    slope_pv2 = (ponto_final_pv2_y - ponto_inicial_pv2_y) / (ponto_final_pv2_x - ponto_inicial_pv2_x)
    for i in range(ponto_inicial_pv2_x + 1, ponto_final_pv2_x + 1):
        y_pv[i] = ponto_inicial_pv2_y + (i - ponto_inicial_pv2_x) * slope_pv2
    y_pv[ponto_final_pv2_x] = ponto_final_pv2_y


# --- 2. EV (Valor Agregado)
x_ev_final = np.linspace(0, semanas_max, int((semanas_max + 1) * 4))
y_ev_final = np.zeros_like(x_ev_final)

# Valores intermediários para as fases de crescimento do EV
ev_crescimento_restante = ev_valor_final - ev_valor_semana9
ev_valor_semana13_5 = ev_valor_semana9 + 0.80 * ev_crescimento_restante # 80% do crescimento

for i, t in enumerate(x_ev_final):
    if t <= 5:
        y_ev_final[i] = t * (ev_valor_semana5 / 5)
    elif t <= 6:
        y_ev_final[i] = ev_valor_semana5
    elif t <= 9:
        slope_ev_6_9 = (ev_valor_semana9 - ev_valor_semana5) / 3
        y_ev_final[i] = ev_valor_semana5 + (t - 6) * slope_ev_6_9
    elif t <= semana_pausa_fim: # 9 a 12.5
        y_ev_final[i] = ev_valor_semana9
    elif t <= semana_crescimento_rapido_fim: # 12.5 a 13.5
        slope_ev_12_5_13_5 = (ev_valor_semana13_5 - ev_valor_semana9) / 1.0
        y_ev_final[i] = ev_valor_semana9 + (t - semana_pausa_fim) * slope_ev_12_5_13_5
    else: # 13.5 a 14
        slope_ev_13_5_14 = (ev_valor_final - ev_valor_semana13_5) / 0.5
        y_ev_final[i] = ev_valor_semana13_5 + (t - semana_crescimento_rapido_fim) * slope_ev_13_5_14

# --- 3. AC (Custo Real) - LÓGICA ATUALIZADA ---
x_ac_final = np.linspace(0, semanas_max, int((semanas_max + 1) * 4))
y_ac_final = np.zeros_like(x_ac_final)

# Valores intermediários para as fases de crescimento do AC
ac_crescimento_restante = ac_valor_final - ac_valor_semana9
ac_valor_semana13_5 = ac_valor_semana9 + 0.80 * ac_crescimento_restante # 80% do crescimento

for i, t in enumerate(x_ac_final):
    if t <= 5:
        y_ac_final[i] = t * (ac_valor_semana5 / 5)
    elif t <= 7.5:
        y_ac_final[i] = ac_valor_semana5
    elif t <= 9:
        slope_ac_7_5_9 = (ac_valor_semana9 - ac_valor_semana5) / 1.5
        y_ac_final[i] = ac_valor_semana5 + (t - 7.5) * slope_ac_7_5_9
    elif t <= semana_pausa_fim: # 9 a 12.5
        y_ac_final[i] = ac_valor_semana9
    elif t <= semana_crescimento_rapido_fim: # 12.5 a 13.5
        slope_ac_12_5_13_5 = (ac_valor_semana13_5 - ac_valor_semana9) / 1.0
        y_ac_final[i] = ac_valor_semana9 + (t - semana_pausa_fim) * slope_ac_12_5_13_5
    else: # 13.5 a 14
        slope_ac_13_5_14 = (ac_valor_final - ac_valor_semana13_5) / 0.5
        y_ac_final[i] = ac_valor_semana13_5 + (t - semana_crescimento_rapido_fim) * slope_ac_13_5_14


# --- Criação do Gráfico ---
plt.figure(figsize=(12, 4))

plt.plot(x_pv, y_pv, label='PV (Valor Planejado)', marker='.', linestyle='-', color='blue')
plt.plot(x_ev_final, y_ev_final, label='EV (Valor Agregado)', linestyle='-', color='green')
plt.plot(x_ac_final, y_ac_final, label='AC (Custo Real)', linestyle='-', color='red')

# Adiciona marcadores apenas nos pontos de semana cheia para EV e AC
x_marcadores = np.arange(0, semanas_max + 1)
y_ev_marcadores = np.interp(x_marcadores, x_ev_final, y_ev_final)
y_ac_marcadores = np.interp(x_marcadores, x_ac_final, y_ac_final)
plt.plot(x_marcadores, y_ev_marcadores, linestyle='None', marker='.', color='green')
plt.plot(x_marcadores, y_ac_marcadores, linestyle='None', marker='.', color='red')

# Configurações do Gráfico
plt.title('Gráfico de Valor Agregado - Até 29/06/2025', fontsize=16)
plt.xlabel('Semanas', fontsize=14)
plt.ylabel('Custo (R$)', fontsize=14)

plt.xlim(0, semanas_max)
plt.ylim(0, orcamento_max * 1.05)

plt.xticks(np.arange(0, semanas_max + 1, 1))
plt.yticks(np.arange(0, orcamento_max + 5000, 5000))

plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# Mostrar o gráfico
plt.show()

# Verificação dos valores finais
print("Valores Finais (Semana 14):")
print(f"PV: R$ {y_pv[-1]:.2f}")
print(f"EV: R$ {y_ev_final[-1]:.2f}")
print(f"AC: R$ {y_ac_final[-1]:.2f}")