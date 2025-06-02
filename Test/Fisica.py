# Inicialização
dist_entre_trens = 60  # km
v_trem = 30            # km/h
v_passaro = 60         # km/h

tempo_total = 0
dist_total_passaro = 0
sentido = "ida"  # começa indo do T1 para o T2

passo = 1
print("Passo a passo do voo do pássaro:\n")

while dist_entre_trens > 0.001:  # tolerância para evitar loop infinito
    if sentido == "ida":
        # trem de destino (T2) vem a 30 km/h
        # velocidade relativa = 60 + 30 = 90 km/h
        tempo = dist_entre_trens / (v_passaro + v_trem)
    else:
        # volta para T1, que também está vindo a 30 km/h
        # velocidade relativa = 60 + 30 = 90 km/h
        tempo = dist_entre_trens / (v_passaro + v_trem)
    
    # distância percorrida pelo pássaro
    dist_voo = v_passaro * tempo
    dist_total_passaro += dist_voo
    tempo_total += tempo
    
    # trens se aproximam
    dist_entre_trens -= 2 * v_trem * tempo  # ambos se movem

    print(f"Passo {passo}:")
    print(f"  Sentido: {sentido}")
    print(f"  Tempo de voo: {tempo:.4f} h")
    print(f"  Distância do voo: {dist_voo:.4f} km")
    print(f"  Distância entre trens agora: {dist_entre_trens:.4f} km")
    print()

    # alterna o sentido
    sentido = "volta" if sentido == "ida" else "ida"
    passo += 1

print(f"Distância total percorrida pelo pássaro: {dist_total_passaro:.4f} km")
print(f"Tempo total até colisão: {tempo_total:.4f} h")