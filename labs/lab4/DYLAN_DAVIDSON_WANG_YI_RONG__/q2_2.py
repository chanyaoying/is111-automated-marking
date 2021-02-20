def  calculate_rows_of_lights(x,y):
    #x budget, y cost
    runningcost = 0
    
    for i in range(1,x//y):
        
        runningcost += i*y
        
        if x < runningcost:
            return i-1
    else:
        return 0

