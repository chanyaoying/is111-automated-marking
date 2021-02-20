def pass_ippt(pushup_score, situp_score, run_score):
    if pushup_score + situp_score + run_score >= 51:
        if pushup_score and situp_score and run_score != 0:
            return True
        else:
            return False
    else:
        return False
print(pass_ippt(10,20,20)==False)
print(pass_ippt(20,0,40)==False)
print(pass_ippt(20,15,33)==True)