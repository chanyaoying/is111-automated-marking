def calculate_row_of_lights(budget,cost_per_light):
    import math
    no_of_lights = math.floor(budget/cost_per_light)
    for i in range(no_of_lights):
        no_of_lights = no_of_lights - (i+1)
        if no_of_lights < 0:
            break
    return i
  