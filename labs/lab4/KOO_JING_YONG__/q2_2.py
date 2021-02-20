#2.2
def calculate_rows_of_lights(budget, cost_per_light):
    no_of_lights= budget//cost_per_light
    row = 0
    while True:
        christmas_light = (row+1)/2*(row+2)
        if no_of_lights > christmas_light:
            row += 1
        else:
            break
    return row
    
pass

#alternative answer
#2.2
def calculate_rows_of_lights(budget, cost_per_light):
    no_of_lights= budget // cost_per_light
    row_of_lights = int(((2 * no_of_lights + 1 / 4) ** 0.5) - 0.5)
    return row_of_lights

pass
