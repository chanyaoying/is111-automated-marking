c = float((input('What is the change? ')))

note10 = c //10
if note10 >0:
    print('$10 notes: ', int(note10))

note5 = c %10 //5
if note5 > 0:
    print ('$5 notes: ', int(note5))

note2 = c %10 %5 //2
if note2 > 0:
    print('$2 notes: ', int(note2))

coindollar = c %10 %5 %2 //1
if coindollar > 0:
    print('$1 coin: ', int(coindollar))

coin10 = c %10 %5 %2 %1 //0.1
if coin10 > 0: 
    print('10 cents coin: ', int(coin10))

coin5 = c %10 %5 %2 %1 %0.1 //0.05
if coin5 > 0:
    print('5 cents coin: ', int(coin5))

coin1 = c %10 %5 %2 %1 %0.1 %0.05 // 0.01
if coin1 > 0:
    print('1 cent coin: ', int(coin1))