def pass_ippt(pushup_score, situp_score, run_score):
    result = False
    if pushup_score > 0 and situp_score > 0 and run_score > 0:
        sum = pushup_score + situp_score + run_score
        if sum >= 51:
            result = True
    return result

pass
