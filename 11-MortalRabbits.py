def DP_rabbits(n,m):
    """
    Starting with 1 pair of rabbits that live for m months, calculate the total number of pairs of rabbits after n month.
    """
    rabbits=[1,1]
    months = 2
    while months < n:
        if months < m:
            rabbits.append(rabbits[-1] + rabbits[-2])
            months += 1
        else:
            m_montholdrabbits=rabbits[-1-m]
            rabbits.append(rabbits[-1] + rabbits[-2] - rabbits[-2])
            rabbits[1] += rabbits[0] - m_montholdrabbits
            months += 1


DP_rabbits(1,89,16)



n = 89 #replace input                                                                        
m = 16 #replace input                                                                       
bunnies = [1, 1]                                                               
months = 2
count = []                                                                     
while months < n:                                                              
    if months < m:                                                             
        bunnies.append(bunnies[-2] + bunnies[-1])                              
    elif months == m or count == m + 1:                                        
        bunnies.append(bunnies[-2] + bunnies[-1] - 1)                          
    else:                                                                      
        bunnies.append(bunnies[-2] + bunnies[-1] - bunnies[-(                  
            m + 1)])                                                           
    months += 1                                                               
print(bunnies[-1])