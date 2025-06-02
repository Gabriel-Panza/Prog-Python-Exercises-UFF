import matplotlib.pyplot as plt
import numpy as np

# --- Parâmetros Globais do Projeto ---
orcamento_max = 43650.00
semanas_max = 14

# --- Parâmetros que definem a forma da curva PV (NÃO ALTERAR ESTES PARA O PV) ---
# O bloco de cálculo do PV abaixo usa diretamente estes valores.
semana_parada_ev_ac_para_pv = 5    # Ponto de inflexão do PV é na semana 5
ev_na_semana_parada_para_pv = 12981.51 # Valor do PV no ponto de inflexão

# --- Parâmetros para o "valor antigo" do AC (ponto de inflexão da nova curva AC) ---
ac_antigo_semana_kink = 5
ac_antigo_valor_kink = 5950.00

# --- NOVOS Parâmetros para as curvas EV e AC atuais ---
nova_semana_parada_ev_ac = 9
novo_ev_na_parada = 23640.84
novo_ac_na_parada = 23625.00


# --- 1. PV (Valor Planejado) - LÓGICA DE CÁLCULO INALTERADA ---
# Este bloco usa 'semana_parada_ev_ac_para_pv' e 'ev_na_semana_parada_para_pv'
# para manter a forma original do PV conforme solicitado.
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


# --- 2. EV (Valor Agregado) - ATUALIZADO ---
x_ev_novo = np.array(range(nova_semana_parada_ev_ac + 1)) # Semanas 0 a 9
y_ev_novo = np.zeros(nova_semana_parada_ev_ac + 1)
if nova_semana_parada_ev_ac > 0:
    slope_ev_novo = novo_ev_na_parada / nova_semana_parada_ev_ac
    for i in range(1, nova_semana_parada_ev_ac + 1):
        y_ev_novo[i] = i * slope_ev_novo
    y_ev_novo[nova_semana_parada_ev_ac] = novo_ev_na_parada
elif nova_semana_parada_ev_ac == 0:
    if len(y_ev_novo) > 0:
         y_ev_novo[0] = novo_ev_na_parada

# --- 3. AC (Custo Real) - ATUALIZADO e Segmentado ---
x_ac_novo = np.array(range(nova_semana_parada_ev_ac + 1)) # Semanas 0 a 9
y_ac_novo = np.zeros(nova_semana_parada_ev_ac + 1)

# Segmento 1 do AC: da semana 0 até ac_antigo_semana_kink (semana 5)
if ac_antigo_semana_kink > 0:
    slope_ac1 = ac_antigo_valor_kink / ac_antigo_semana_kink
    for i in range(ac_antigo_semana_kink + 1):
        y_ac_novo[i] = i * slope_ac1
    y_ac_novo[ac_antigo_semana_kink] = ac_antigo_valor_kink
elif ac_antigo_semana_kink == 0:
     if len(y_ac_novo) > 0: # Should be y_ac_novo, not y_ac
        y_ac_novo[0] = ac_antigo_valor_kink

# Segmento 2 do AC: de ac_antigo_semana_kink até nova_semana_parada_ev_ac (semana 9)
if nova_semana_parada_ev_ac > ac_antigo_semana_kink:
    delta_ac_segmento2 = novo_ac_na_parada - ac_antigo_valor_kink
    delta_semanas_segmento2 = nova_semana_parada_ev_ac - ac_antigo_semana_kink
    
    if delta_semanas_segmento2 > 0:
        slope_ac2 = delta_ac_segmento2 / delta_semanas_segmento2
        for i in range(ac_antigo_semana_kink + 1, nova_semana_parada_ev_ac + 1):
            y_ac_novo[i] = ac_antigo_valor_kink + (i - ac_antigo_semana_kink) * slope_ac2
    y_ac_novo[nova_semana_parada_ev_ac] = novo_ac_na_parada
elif nova_semana_parada_ev_ac == ac_antigo_semana_kink: # Caso a nova parada seja no kink
    y_ac_novo[nova_semana_parada_ev_ac] = novo_ac_na_parada # Usa o valor final para essa semana

# --- Criação do Gráfico ---
plt.figure(figsize=(12, 4))

plt.plot(x_pv, y_pv, label='PV (Valor Planejado)', marker='.', linestyle='-', color='blue')
plt.plot(x_ev_novo, y_ev_novo, label='EV (Valor Agregado)', marker='.', linestyle='-', color='green') # Usar novos dados EV
plt.plot(x_ac_novo, y_ac_novo, label='AC (Custo Real)', marker='.', linestyle='-', color='red')       # Usar novos dados AC

# Configurações do Gráfico
plt.title('Gráfico de Valor Agregado - Até 01/06/2025', fontsize=16) # Título atualizado
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
plt.savefig('grafico_valor_agregado_dados_atuais.png') # Nome do arquivo atualizado
plt.show()

# Verificação dos valores na nova semana de parada
print(f"Valores na Semana {nova_semana_parada_ev_ac}:")
pv_na_nova_parada = 0
if nova_semana_parada_ev_ac < len(y_pv):
    pv_na_nova_parada = y_pv[nova_semana_parada_ev_ac]

print(f"PV na semana {nova_semana_parada_ev_ac}: R$ {pv_na_nova_parada:.2f}")
print(f"EV na semana {nova_semana_parada_ev_ac}: R$ {novo_ev_na_parada:.2f}")
print(f"AC na semana {nova_semana_parada_ev_ac}: R$ {novo_ac_na_parada:.2f}")

# Verificação do ponto de inflexão do AC
print(f"\nValores no ponto de inflexão do AC (Semana {ac_antigo_semana_kink}):")
print(f"AC na semana {ac_antigo_semana_kink}: R$ {y_ac_novo[ac_antigo_semana_kink]:.2f} (Esperado: R$ {ac_antigo_valor_kink:.2f})")