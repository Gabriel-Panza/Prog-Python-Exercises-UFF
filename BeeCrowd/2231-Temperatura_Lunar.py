def calculate_temperature_averages(temperatures, interval):
    n = len(temperatures)
    sum_interval = sum(temperatures[:interval])
    averages = [sum_interval // interval]

    for i in range(0, n - interval):
        sum_interval += temperatures[i + interval] - temperatures[i]
        averages.append(sum_interval // interval)

    return averages

N_Temperatures, M_intervals = map(int, input().split())
cont = 1

while N_Temperatures != 0 and M_intervals != 0:
    temperatures = [int(input()) for i in range(N_Temperatures)]
    
    min_average, max_average = min(calculate_temperature_averages(temperatures, M_intervals)), max(calculate_temperature_averages(temperatures, M_intervals))
    
    print("Teste", cont)
    print(min_average, max_average)
    print()
    cont += 1
    
    N_Temperatures, M_intervals = map(int, input().split())