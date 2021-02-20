def calculate_rows_of_lights(budget, cost_per_light):    
    if cost_per_light > budget:
        return 0
    
    max_lights = budget // cost_per_light
    number_of_lights = 0

    for i in range( 1, max_lights ):
        number_of_lights += i    #accumulating lights needed after each row is added

        if number_of_lights > max_lights:
            number_of_rows = i - 1
            break 
            
    return number_of_rows


print(calculate_rows_of_lights(50,2) == 6)
print(calculate_rows_of_lights(100,3) == 7)
print(calculate_rows_of_lights(10,12) == 0)
