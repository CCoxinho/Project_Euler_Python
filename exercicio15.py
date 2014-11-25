def fact(n):
    f = 1
    for x in range(1, n + 1):
        f = f * x
    return f

y = (fact(40) / fact(20) / fact(20))
z = int(y)
print(z)
