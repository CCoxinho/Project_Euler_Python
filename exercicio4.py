def palindromo():
    n=0
    for i in range(100, 999):
        for j in range(i+1, 999):
            p = i * j
            if p > n:
                s = str(i * j)
                if s == s[::-1]:
                    n=i*j
    print (n)
