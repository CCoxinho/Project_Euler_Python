import math

def digit_powers(expoente):
    if expoente <= 1:
        print('O número não é válido')

    powers = {}
    resultado = 0
    for a in range(10):
        powers[a] = a ** expoente
    teste = (expoente + 1) * (9 ** expoente)

    for i in range(10, teste):
        guarda = i
        total = 0

        for _ in range(int(math.log10(i)) + 1):
            digit =i % 10
            total += powers[digit]
            i //= 10

        if (total == guarda):
            resultado += total

    print(resultado)
