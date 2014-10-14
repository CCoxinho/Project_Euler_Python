def primo(n,i):
    while i*i<n:
        while n%i==0:
            n=n/i
        i=i+1
    return (n)
#n = 600851475143
#i = 2
