def pass_ippt (pushup_score, situp_score, run_score):
    total_score = pushup_score + situp_score + run_score
    if pushup_score == 0 or situp_score == 0 or run_score == 0 or total_score < 51:
        return False
    if pushup_score > 0 and situp_score > 0 and run_score > 0 and total_score > 50:
        return True
   

    