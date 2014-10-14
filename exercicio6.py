def diferenca():
    i=0
    soma1=[]
    soma2=[]
    for i in range(101):
        x=i**2
        soma1.append(x)
        i++1
    for i in range(101):
        soma2.append(i)
        i++1
    somadosquadrados=sum(soma1)
    quadradodassomas=sum(soma2)
    quadradodassomas=quadradodassomas**2
    return quadradodassomas-somadosquadrados
        
        
    
