# question 1.2 

def mask_email(email):
    return '*' * (len(email)-10) + str(email)[-10:]

print(mask_email('abcdef@gmail.com') == '******@gmail.com')
print(mask_email('is111@gmail.com') == '*****@gmail.com')