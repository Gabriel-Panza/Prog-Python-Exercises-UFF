# Para caso a lista venha vazia - Metodo sem usar map
lista = []

while True:
    if len(lista)>=10:
        break
    
    aluno_que_ja_esta_na_fila = int(input("Me informe a sua matricula: "))
    lista.append(aluno_que_ja_esta_na_fila)
    
    lugar = input("Você está guardando lugar? S para sim e N para não\n")
    qntd = int(input("Informe quantos amigos voce está guardando lugar"))
    if (lugar == 'S'):
        if (qntd>3):
            qntd = 3
        for i in range(qntd):
            alunos_que_entrara_na_fila = int(input("Informe a matricula do seu amigo: "))
            lista.append(alunos_que_entrara_na_fila)
        
    resposta = input("Voce vai continuar na fila? S para sim e N para não\n")
    if (resposta == 'N'):
        lista.remove(aluno_que_ja_esta_na_fila)
    
if len(lista)>10: 
    lista = lista[0:10]
for aluno in lista:
    print(aluno)
    
# Para caso a lista venha vazia - Metodo usando map
##lista = []

# while True:
#     if len(lista)>=10:
#         break
    
#     aluno_que_ja_esta_na_fila = int(input("Me informe a sua matricula: "))
#     lista.append(aluno_que_ja_esta_na_fila)
    
#     alunos_que_entrarao_na_fila = []
#     lugar = input("Você está guardando lugar? S para sim e N para não\n")
#     if (lugar == 'S'):
#         alunos_que_entrarao_na_fila = list(map(int, input("Informe a matricula dos alunos que você está guardando lugar\n").split(" ")))
#         if len(alunos_que_entrarao_na_fila)>3:
#             alunos_que_entrarao_na_fila = alunos_que_entrarao_na_fila[0:3]
    
#     for matricula in alunos_que_entrarao_na_fila:
#         lista.append(matricula)
        
#     resposta = input("Voce vai continuar na fila? S para sim e N para não\n")
#     if (resposta == 'N'):
#         lista.remove(aluno_que_ja_esta_na_fila)
    
# if len(lista)>10: 
#     lista = lista[0:10]
# for aluno in lista:
#     print(aluno)


# Para caso a lista venha preenchida com alunos
# lista = []
# for i in range(50):
#     lista.append(i)

# contador=0
# while True:
#     if len(lista)>=10:
#         break
    
#     lugar = input(f"Aluno {lista[contador]} está guardando lugar? S para sim e N para não\n")
#     qntd = int(input("Informe quantos amigos voce está guardando lugar"))
#     if (lugar == 'S'):
#         if (qntd>3):
#             qntd = 3
#         lista_aluno = lista[0:contador+1]
#         lista_restante = lista[contador+1:len(lista)]
#         for i in range(qntd):
#             alunos_que_entrara_na_fila = int(input("Informe a matricula do seu amigo: "))
#             lista_aluno.append(alunos_que_entrara_na_fila)
#         lista = lista_aluno + lista_restante  
        
#     resposta = input("Voce vai continuar na fila? S para sim e N para não\n")
#     if (resposta == 'N'):
#         lista.remove(aluno_que_ja_esta_na_fila)
#     contador+=1

# if len(lista)>10: 
#     lista = lista[0:10]
# for aluno in lista:
#     print(aluno)