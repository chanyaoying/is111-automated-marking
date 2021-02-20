def get_num_solutions(a,b,c):

    if b**2-4*a*c>0:
        return 2
    elif b**2-4*a*c == 0:
        return 1
    else:
        return 0

print(get_num_solutions(4,5,6) == 0)
print(get_num_solutions(3,6,3) == 1)
print(get_num_solutions(2,4,1) == 2)
