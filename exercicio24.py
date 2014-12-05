from itertools import permutations

def lexicographic_permotations():
    for (a, b) in enumerate(permutations('0123456789')):
        if a == 999999: 
            resultado = (''.join(b))
            print(resultado)
            break
