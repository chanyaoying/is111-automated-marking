def pass_ippt(pushup_score, situp_score, run_score):
    total_score = pushup_score + situp_score + run_score
    if total_score >= 51 and pushup_score > 0 and situp_score >0 and run_score >0:
        return True
    else:
        return False
    
print(pass_ippt(10,20,20) == False)
print(pass_ippt(20,0,40) == False)
print(pass_ippt(20,15,33) == True)