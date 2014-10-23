def factorial(number):
    x = 1
    for i in range(number):
        x = x*(i+1)
    a = list(str(x))
    b = sum(int(number) for number in a)
    print (b)


#number=100
