
if level == 'Member' or level == 'Silver':
    if payment == 'GrabPay':
        points = fare * 3
    else:
        points = fare
if level == 'Gold':
    if payment == 'GrabPay':
        points = fare * 4.5
    else:
        points = fare * 1.5
if level == 'Platinum':
    if payment == 'GrabPay':
        points = fare * 6
    else: 
        points = fare * 2
import math     
