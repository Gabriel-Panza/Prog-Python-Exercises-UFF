N = int(input())                            
D = []                                      
minor = 100000 
for i in range(1,N+1):
    index = input()                        
    M = int(index.split()[0])              
    list = list(map(int, index.split()))  
    t_up = 0
    t_down = 0
    
    for j in range(0,len(list)-1):
        trilha = list[j+1] - list[j]
        if trilha > 0:     
            t_up += trilha          
        if trilha < 0:     
            t_down += trilha          
    t_down *= -1                         
    if t_up < t_down :              
        D.append(t_up)
    else:                                 
        D.append(t_down)
        
for y in range(0, len(D)):                 
   if D[y] < minor :                    
       minor = D[y]                       
       best_trilha = y + 1            
print(best_trilha)