def soma_multiplos():
    lista=[]
    for i in range (3, 1000):
        if i%3==0 or i%5==0:
            lista.append(i)
    
    return sum(lista)
