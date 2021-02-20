#1.1

def mask_mobile(x):
    x = str(x)
    res= ""
    for i in range(len(x)):
        if i >= len(x)-4:
            res += x[i]
        else:
            res += "*"
    return res

mask_mobile('12345678'
            
#1.2
def mask_email(x):
    result =''
    for i in range(len(x)):
        if x[i] == '@':
            break
        result += "*"
    for ch in range (i,len(x)):
        result += x[ch]
    return result

mask_email('abcdef@gmail.com')
         
#1.3
def get_num_solutions (a,b,c):
    ans = ((b**2)-(4*a*c))
    if ans > 0:
        return 2
    elif ans == 0:
        return 1
    else:
        return 0
    
print(get_num_solutions(4,5,6))