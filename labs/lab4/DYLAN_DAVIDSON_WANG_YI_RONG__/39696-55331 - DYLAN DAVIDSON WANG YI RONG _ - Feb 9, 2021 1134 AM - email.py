def mask_email(x):
    y = x.find('@')
    print (x[:y])

x = 'wzxjcnasj@mail.com'
mask_email(x)