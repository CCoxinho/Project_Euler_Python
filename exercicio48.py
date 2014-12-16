def self_powers():
    total = 0
    for i in range(1, 1001):
        total = total + (i ** i)
    x = str(total)
    y = len(x) - 10
    resultado = x[y:]
    print (resultado)
