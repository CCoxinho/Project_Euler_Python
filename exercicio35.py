def primo(n):
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True

def rotaçao(n):
    yield n
    n = str(n)
    for i in range(len(n) - 1):
        n = n[1:] + n[0]
        return int(n)

def circular(n):
    for i in rotaçao(n):
        if not primo(i):
            return False
    return True

print (len([i for i in range(2, 1000000) if circular(i)]))
