#  question 2.1

def pass_ippt(pushup_score, situp_score, run_score):
    if pushup_score >= 1 and situp_score >= 1 and run_score >=1 and pushup_score + situp_score + run_score >= 51:
        return True
    return False

