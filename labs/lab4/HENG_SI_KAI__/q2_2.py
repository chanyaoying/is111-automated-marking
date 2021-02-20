def calculate_rows_of_lights(budget, cost_per_light):
    rows_of_lights = 0
    no_of_lights = budget // cost_per_light
    while no_of_lights > 0:
        no_of_lights -= (rows_of_lights + 1)
        if no_of_lights < 0:
            break
        rows_of_lights += 1
    return rows_of_lights




#     rows -= 1