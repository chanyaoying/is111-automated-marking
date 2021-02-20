def calculate_rows_of_lights(budget, cost_per_light):
    no_of_lights=budget//cost_per_light
    used_lights=0
    for i in range(0, no_of_lights+2):
        used_lights+=i
        if used_lights>no_of_lights:
            return i-1
            break
