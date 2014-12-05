def distinct_powers():
    L = [] 
 
    for a in range(2, 101):
        for b in range(2, 101):
            c = a**b
            if c in L:
                pass
            else:
                L.append(c)
 
    print ((len(L)))
