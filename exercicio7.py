def primo():
    primos = []
    primos.append(2)
    n = 3
    count = 1
    found = False
    while found == False:
        for x in primos:
            if n%x == 0:
                found = False
                break
                
            else:
                if x == primos[-1]:
                    primos.append(n)
                    count += 1
        n += 1
        if count == 10001:
            found = True
    print(primos[-1]) 

        
                
   

        
                
   
