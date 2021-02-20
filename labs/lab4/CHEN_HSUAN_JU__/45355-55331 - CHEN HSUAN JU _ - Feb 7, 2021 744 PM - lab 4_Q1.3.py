import math

def get_num_solutions(a, b, c):
    quadratic = b**2 - 4*a*c
    if quadratic > 0:
        return 2
    if quadratic == 0:
        return 1
    else:
        return 0

print(get_num_solutions(2,4,1))