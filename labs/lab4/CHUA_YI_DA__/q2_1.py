#2.1 
def pass_ippt(pushup_score,situp_score,run_score):
    if pushup_score == 0 or situp_score == 0 or run_score == 0:
        result = False 
    elif pushup_score + situp_score + run_score >= 51:
        result = True
    else:
        result = False
    return result 

#test cases
