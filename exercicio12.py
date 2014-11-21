import math

def highly_divisible():
    l = []
    one = 0
    a = 1
    b = 2
    while one == 0:
        a = a + b 
        b += 1
        l = []

        sqrt_a = int(math.sqrt(a))

        for x in range(1, sqrt_a + 1):
            if a % x == 0:
                l.append(x)
                if x < math.sqrt(a):
                    l.append(a // x)
                if len(l) > 500:
                    print(a)
                    one = 1
                else:
                    break
    print(a)

