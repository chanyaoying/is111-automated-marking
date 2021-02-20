
def pass_ippt(pushup_score,situp_score,run_score):
    if pushup_score == 0 or situp_score == 0 or run_score == 0:
        return False
    total =  pushup_score + situp_score + run_score
    if total < 51:
        return False
    else:
        return True

pass
pass
pass
