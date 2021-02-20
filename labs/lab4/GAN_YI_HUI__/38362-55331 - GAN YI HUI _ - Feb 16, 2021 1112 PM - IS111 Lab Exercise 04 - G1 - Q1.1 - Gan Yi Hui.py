# question 1.1

def mask_mobile(num):
    return '*' * 4 + str(num)[4:]

print(mask_mobile(87654321) == '****4321')
print(mask_mobile(91234567) == '****4567')