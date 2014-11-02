def longest_collatz():
    maior = 0
    maior_sequencia = 0
    x = dict()
    for n in range(2, 1000001):
        number = n
        contador = 0
        while number > 1:
            try:
                contador += x[number] - 1
                break
            except KeyError:
                pass
             
            if number % 2 == 0:
                number = number / 2
            else:
                number = number * 3 + 1
            contador += 1
 
        contador += 1
        x[n] = contador
 
        if contador > maior_sequencia:
            maior_sequencia = contador
            maior = n
 
    print (maior)
    print (maior_sequencia)
     

