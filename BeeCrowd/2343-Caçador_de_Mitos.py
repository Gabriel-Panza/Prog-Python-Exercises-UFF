N =  int(input())                           
vectCoordinates = []                        
alreadyGone = [0]*N                               
contF = 0                                  
for i in range(N):
    coordinates = []
    x,y = map(int,input().split())         
    coordinates.append(x)                   
    coordinates.append(y)                  
    vectCoordinates.append(coordinates)      

    if vectCoordinates[i] not in alreadyGone:     
        alreadyGone[i] = vectCoordinates[i]
    else:                                  
        contF+= 1

if contF > 0:                               
    print(1)
else:                                      
    print(0)