def pass_ippt(pushup_score,situp_score,run_score):
    total = 0
    passing = False
    if pushup_score >= 1 and pushup_score <= 25:
        total += 1
    if situp_score >= 1 and situp_score <= 25:
        total += 1
    if run_score >= 1 and run_score <= 25:
        total += 1
    if total >= 51:
        passing = True
    return passing

print(pass_ippt(20,0,40) == False)