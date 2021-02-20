#2.2
def calculate_rows_of_lights(budget,cost_per_light):
    total_lights = budget//cost_per_light
    num_of_rows = 0 
    if total_lights == 0:
        num_of_rows = 0
    else:
        while num_of_rows >= 0:
            num_of_rows += 1
            total_lights -= num_of_rows
            if total_lights - num_of_rows < 0:
                break 
    return num_of_rows

#test cases
