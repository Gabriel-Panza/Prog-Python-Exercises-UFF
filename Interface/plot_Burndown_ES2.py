import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

def gerar_grafico_burndown(esforco_planejado_restante, esforco_real_restante, titulo="Gráfico de Burndown"):
    """
    Gera um gráfico de burndown.

    Args:
        esforco_planejado_restante (list): Lista do esforço restante planejado para cada período.
                                          Para 5 semanas, deve ter 6 elementos (Semana 0 a Semana 5).
                                          Ex: [100, 80, 60, 40, 20, 0]
        esforco_real_restante (list): Lista do esforço restante real para cada período.
                                     Para 5 semanas, deve ter 6 elementos.
                                     Ex: [100, 90, 70, 50, 10, 0]
        titulo (str, optional): Título do gráfico. Default é "Gráfico de Burndown".
    """
    if not esforco_planejado_restante or not esforco_real_restante:
        print("Erro: As listas de esforço não podem estar vazias.")
        return

    if len(esforco_planejado_restante) != len(esforco_real_restante):
        print("Erro: As listas de esforço planejado e real devem ter o mesmo tamanho.")
        return

    # Número de períodos (semanas neste caso).
    # Se a lista tem 6 elementos (S0 a S5), range(6) -> [0, 1, 2, 3, 4, 5]
    periodos = list(range(len(esforco_planejado_restante)))

    # Cria o gráfico
    plt.figure(figsize=(10, 6))

    # Linha de esforço planejado (ideal)
    plt.plot(periodos, esforco_planejado_restante, marker='o', linestyle='--', color='red', label='Esforço Planejado')

    # Linha de esforço real
    plt.plot(periodos, esforco_real_restante, marker='o', linestyle='-', color='green', label='Esforço Real')

    # Títulos e legendas
    plt.title(titulo)
    plt.xlabel("Tempo da Sprint (Semanas)") # Eixo X modificado
    plt.ylabel("Esforço (Homem-Hora)") # Eixo Y modificado
    plt.legend()
    plt.grid(True)

    # Ajustar os ticks do eixo x para serem inteiros (representando as semanas)
    ax = plt.gca()
    ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    ax.set_xticks(periodos) # Garante que todos os pontos de semana sejam mostrados se houver espaço

    # Garantir que o eixo Y comece em 0 e vá um pouco além do máximo, se necessário
    max_effort_values = []
    if esforco_planejado_restante:
        max_effort_values.extend(esforco_planejado_restante)
    if esforco_real_restante:
        max_effort_values.extend(esforco_real_restante)
    
    if not max_effort_values: # Caso ambas as listas estejam vazias (já tratado, mas por segurança)
        max_effort = 10 
    else:
        max_effort = max(max_effort_values)

    plt.ylim(bottom=0, top=max_effort * 1.1 if max_effort > 0 else 10)
    plt.xlim(left=min(periodos)-0.1 if periodos else 0, right=max(periodos)+0.1 if periodos else 1)


    # Mostrar o gráfico
    plt.tight_layout() # Ajusta o layout para evitar sobreposições
    plt.show()


# Exemplo: Projeto correndo como esperado ao longo de 5 semanas
print("Gerando 'Sprint 1' de 5 semanas sem atraso")
# Esforço planejado restante ao final de cada semana (Semana 0 é o início)
planejado_semanal = [126.0, 100.8, 75.6, 50.4, 25.2, 0]
# Esforço real restante ao final de cada semana
real_semanal = [126.0, 77.0, 77.0, 77.0, 35.0, 0]
gerar_grafico_burndown(planejado_semanal, real_semanal, "Burndown da Sprint 1 (5 Semanas)")

# Exemplo 2: Projeto atrasado em uma sprint de 5 semanas
print("\nGerando 'Sprint 2' de 4 semanas com Atraso")
# Esforço planejado restante ao final de cada semana (Semana 0 é o início)
planejado_semanal_atraso = [105, 78.75, 52.5, 26.25, 0]
# Esforço real restante ao final de cada semana
real_semanal_atraso = [105, 105, 105, 52.5, 26.25]
gerar_grafico_burndown(planejado_semanal_atraso, real_semanal_atraso, "Burndown da Sprint 2 (4 Semanas) - Atrasado")