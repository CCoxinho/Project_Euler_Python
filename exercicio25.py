import math
def first_term_1000():
    a = 0
    b = 1
    n = 1

    while math.log(b, 10) < 999:
        n += 1
        c = a+b
        a = b
        b = c

    print (n)
