def palindromo_decimal(n):
    return n == int(''.join(reversed(str(n))))

def palindromo_binomial(n):
    b = bin(n)[2:]
    return b == ''.join(reversed(b))

print (sum((n for n in range(1, 1000000) if palindromo_decimal(n) and palindromo_binomial(n))))
