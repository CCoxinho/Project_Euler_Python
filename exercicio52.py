def mesmos_numeros(a,b):
    a = list(str(a))
    b = list(str(b))
    found = False
    for i in a:
        for j in range(len(b)):
            if b[j] == i:
                del(b[j])
                found = True
                break
        if not found:
            return False
    if len(b) == 0:
        return True
    else:
        return False

foundz = False
i = 1
while not foundz:
    foundx = True
    for x in range(2,7):
        if not mesmos_numeros(i, i*x):
            foundx = False
            break
    if foundx:
        print (i)
        foundz = True
    i += 1
        
            
                       
