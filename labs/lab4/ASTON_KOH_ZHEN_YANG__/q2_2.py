def calculate_rows_of_lights(budget, cost_per_light):
    number_of_lights = int(budget//cost_per_light)
    number_of_rows = 0
    count_increments = 1
    lights_used = 0
    for i in range(number_of_lights):
        lights_used += count_increments
        if number_of_lights - lights_used >= 0:
            number_of_rows += 1
            count_increments += 1
            
    return number_of_rows

pass
