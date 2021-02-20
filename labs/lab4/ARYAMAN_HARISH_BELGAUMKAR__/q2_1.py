def pass_ippt(pushup_score,situp_score,run_score):
    total_score = pushup_score + situp_score + run_score
    if pushup_score < 0 or situp_score < 0 or run_score < 0 or total_score > 100:
        print("Invalid parameters observed. Recheck!")
    if pushup_score >= 1 and situp_score >= 1 and run_score >= 1 and total_score >= 51:
        return True
    else:
        return False 