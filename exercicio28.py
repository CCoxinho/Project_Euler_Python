def problem_28():
    j = 1
    for i in range(3,1002,2):
        j += (4*i**2-6*(i-1))
    return j
