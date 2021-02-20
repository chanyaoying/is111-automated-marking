y = int(input('What is your chargeable income? '))

if y < 20000:
    t = 0
elif y <= 30000:
    t = 0 + (y - 20000)* 0.02
elif y <= 40000:
    t = 200 + (y -30000)* 0.035
elif y <= 80000:
    t = 550 + (y - 40000)* 0.07
elif y <= 120000: 
    t = 3350 + (y - 80000)* 0.115
elif y <= 160000:
    t = 7950 + (y - 120000)* 0.15
elif y <= 200000:
    t = 13950 + (y - 160000)* 0.18
elif y <= 240000:
    t = 21150 + (y - 200000)* 0.19
elif y <= 280000:
    t = 28750 + (y - 78000)* 0.195
elif y <= 320000:
    t = 36550 + (y - 280000)* 0.20
else: 
    t = 44550 + (y - 320000)* 0.22 
    
print ('Your annual tax is $ {:.2f}'.format(t))