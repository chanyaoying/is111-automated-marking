#IPPT Passing Criteria

def pass_ippt(pushup_score,situp_score,run_score):
    '''Takes in 3 integer parameters pushup_score, situp_score and run_score.
    The function pass_ippt should return True if the NSman has passed his IPPT
    (based on the two criteria mentioned above), and False if the NSman has failed his IPPT.'''
    #Preventing going beyond the max score
    real_pushup = min(25,pushup_score)
    real_situp = min(25, situp_score)
    real_run = min(50,run_score)

    #Calculate total score
    total_score = real_pushup + real_situp + real_run

    #Logic test to check if NSMan passes IPPT
    if real_pushup < 1 or real_situp < 1 or real_run < 1:
        return False
    elif total_score < 51:
        return False
    else:
        return True

print(pass_ippt(10,20,20))
print(pass_ippt(20,0,40))
print(pass_ippt(20,15,33))