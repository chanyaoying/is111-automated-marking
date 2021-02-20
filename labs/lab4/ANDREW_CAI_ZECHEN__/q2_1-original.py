
def pass_ippt(pushup_score,situp_score,run_score):
    if pushup_score == 0 or situp_score == 0 or run_score == 0:
        return False
    total =  pushup_score + situp_score + run_score
    if total < 51:
        return False
    else:
        return True

print(pass_ippt(10,20,20) == False)
print(pass_ippt(20,0,40) == False)
print(pass_ippt(20,15,33) == True)