def soma_fibonacci(n):
    soma=0
    x, y = 0, 1
    while y < n: 
        x, y = y, x+y
        if y%2 == 0:
            soma = soma+y
    return soma
