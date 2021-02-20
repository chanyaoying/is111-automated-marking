#Christmas Tree Lights

def calculate_rows_of_lights(budget,cost_per_light):
    
    #Formula for number of lights
    num_of_lights = budget // cost_per_light

    #Initializing variables
    light_num = 0
    light_row = 0

    #For loop to calculate number of rows
    for i in range(num_of_lights):
        if light_num < num_of_lights:
            light_row += 1
            light_num += i
        else:
            light_row -= 1
            break
    if num_of_lights - light_num < 0:
        light_row = light_row - 1
    
    return light_row