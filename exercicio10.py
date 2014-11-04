import math
def soma_primos():
    soma = []
    soma.append(2)
    for n in range(3, math.sqrt(2000000)):
        primo = True
        for x in range(2, n):
            if math.sqrt(n)%x == 0:
                primo = False
                break
        if primo == True:
            soma.append(n)
    
    print (sum(soma))

   

        
                
   
