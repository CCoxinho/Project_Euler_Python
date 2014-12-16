def powerful_digit():
    resultado = 0
    for i in range(1, 101):
        for j in range(1, 101):
            numero = i ** j
            L = list(str(numero))
            soma = 0
            for z in L:
                soma = soma + int(z)
            if soma > resultado:
                resultado = soma
    print (resultado)
 
