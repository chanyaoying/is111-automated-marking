
#Q1.1

#solution 1
def mask_mobile(mobile_num):
    mobile_num = str(mobile_num)
    for i in mobile_num[:4]:
        mobile_num = mobile_num.replace(i, 'x')
    return mobile_num

#solution 2
def mask_mobile2(mobile_num):
    return '*'*4+str(mobile_num)[4:]


