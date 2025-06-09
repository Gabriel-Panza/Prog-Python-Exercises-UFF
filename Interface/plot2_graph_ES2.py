import matplotlib.pyplot as plt
import numpy as np

# --- Parâmetros Globais do Projeto ---
orcamento_max = 43650.00
semanas_max = 14

# --- Parâmetros que definem a forma da curva PV ---
semana_parada_ev_ac_para_pv = 5
ev_na_semana_parada_para_pv = 12981.51

# --- Parâmetros para o "valor antigo" do AC (ponto de inflexão da nova curva AC) ---
ac_antigo_semana_kink = 5
ac_antigo_valor_kink = 5950.00

# --- NOVOS Parâmetros para as curvas EV e AC atuais ---
nova_semana_parada_ev_ac = 9
novo_ev_na_parada = 24941.61
novo_ac_na_parada = 23625.00

# --- 1. PV (Valor Planejado) ---
x_pv = np.array(range(semanas_max + 1))
y_pv = np.zeros(semanas_max + 1)

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

# --- 2. EV (Valor Agregado) - NOVA LÓGICA COM 3 SEGMENTOS ---
x_ev_novo = np.array(range(nova_semana_parada_ev_ac + 1))  # Semanas 0 a 9
y_ev_novo = np.zeros(nova_semana_parada_ev_ac + 1)

# Segmento 1: semana 0 a 5 - crescimento linear até 12.981,51
if semana_parada_ev_ac_para_pv > 0:
    slope_ev1 = ev_na_semana_parada_para_pv / semana_parada_ev_ac_para_pv
    for i in range(semana_parada_ev_ac_para_pv + 1):
        y_ev_novo[i] = i * slope_ev1
    y_ev_novo[semana_parada_ev_ac_para_pv] = ev_na_semana_parada_para_pv

# Segmento 2: semana 5 a 6 - valor constante
for i in range(semana_parada_ev_ac_para_pv + 1, 7):  # Apenas semana 6
    y_ev_novo[i] = ev_na_semana_parada_para_pv

# Segmento 3: semana 6 a 9 - crescimento até 24.941,61
delta_ev = novo_ev_na_parada - ev_na_semana_parada_para_pv
semanas_segmento3 = 3  # de semana 6 até 9
slope_ev3 = delta_ev / semanas_segmento3
for i in range(7, 10):  # semanas 7, 8, 9
    y_ev_novo[i] = ev_na_semana_parada_para_pv + (i - 6) * slope_ev3

# Garante o valor final exato na semana 9
y_ev_novo[nova_semana_parada_ev_ac] = novo_ev_na_parada

# --- 3. AC (Custo Real) - NOVA LÓGICA: estabilidade de 5 a 7.5 e crescimento até 9 ---
x_ac_novo = np.linspace(0, nova_semana_parada_ev_ac, int((nova_semana_parada_ev_ac + 1) * 2))  # usa intervalos de 0.5 semana
y_ac_novo = np.zeros_like(x_ac_novo)

# Segmento 1: 0 até 5 - crescimento linear até o valor do kink
for i in range(len(x_ac_novo)):
    if x_ac_novo[i] <= ac_antigo_semana_kink:
        y_ac_novo[i] = x_ac_novo[i] * (ac_antigo_valor_kink / ac_antigo_semana_kink)

# Segmento 2: 5 até 7.5 - valor constante (5950.00)
for i in range(len(x_ac_novo)):
    if 5 < x_ac_novo[i] <= 7.5:
        y_ac_novo[i] = ac_antigo_valor_kink

# Segmento 3: 7.5 até 9 - crescimento até novo_ac_na_parada
valor_inicial_segmento3 = ac_antigo_valor_kink
tempo_inicial_segmento3 = 7.5
tempo_final_segmento3 = nova_semana_parada_ev_ac
delta_tempo = tempo_final_segmento3 - tempo_inicial_segmento3
delta_valor = novo_ac_na_parada - valor_inicial_segmento3
slope_ac3 = delta_valor / delta_tempo

for i in range(len(x_ac_novo)):
    if x_ac_novo[i] > 7.5:
        y_ac_novo[i] = valor_inicial_segmento3 + (x_ac_novo[i] - tempo_inicial_segmento3) * slope_ac3

# --- Criação do Gráfico ---
plt.figure(figsize=(12, 4))

plt.plot(x_pv, y_pv, label='PV (Valor Planejado)', marker='.', linestyle='-', color='blue')
plt.plot(x_ev_novo, y_ev_novo, label='EV (Valor Agregado)', marker='.', linestyle='-', color='green')
plt.plot(x_ac_novo, y_ac_novo, label='AC (Custo Real)', linestyle='-', color='red')

# Adiciona marcadores apenas nos pontos de semana cheia (inteiros)
x_ac_marcadores = np.arange(0, nova_semana_parada_ev_ac + 1)
y_ac_marcadores = np.interp(x_ac_marcadores, x_ac_novo, y_ac_novo)
plt.plot(x_ac_marcadores, y_ac_marcadores, linestyle='None', marker='.', color='red')

# Linhas de referência para facilitar a leitura
plt.axvline(5, color='gray', linestyle='--', alpha=0.5)
plt.axvline(7, color='gray', linestyle='--', alpha=0.5)

# Configurações do Gráfico
plt.title('Gráfico de Valor Agregado - Até 01/06/2025', fontsize=16)
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
plt.savefig('grafico_valor_agregado_dados_atuais.png')
plt.show()

# Verificação dos valores
print(f"Valores na Semana {nova_semana_parada_ev_ac}:")
if nova_semana_parada_ev_ac < len(y_pv):
    pv_na_nova_parada = y_pv[nova_semana_parada_ev_ac]
else:
    pv_na_nova_parada = 0

print(f"PV na semana {nova_semana_parada_ev_ac}: R$ {pv_na_nova_parada:.2f}")
print(f"EV na semana {nova_semana_parada_ev_ac}: R$ {novo_ev_na_parada:.2f}")
print(f"AC na semana {nova_semana_parada_ev_ac}: R$ {novo_ac_na_parada:.2f}")

print(f"\nValores no ponto de inflexão do AC (Semana {ac_antigo_semana_kink}):")
print(f"AC na semana {ac_antigo_semana_kink}: R$ {y_ac_novo[ac_antigo_semana_kink]:.2f} (Esperado: R$ {ac_antigo_valor_kink:.2f})")