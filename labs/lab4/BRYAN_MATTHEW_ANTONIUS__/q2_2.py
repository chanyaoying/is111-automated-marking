def calculate_rows_of_lights (budget, cost_per_light):
    rows = 1
    if budget < cost_per_light or budget <= 0 or cost_per_light <= 0:
        return (0)
    else:
        for no_of_lights in range (1,100):
            budget = budget - no_of_lights*cost_per_light
            if budget < no_of_lights*cost_per_light:
                break
            else:
                rows += 1
    return rows

print(calculate_rows_of_lights(50,2) == 6)
print(calculate_rows_of_lights(100,3) == 7)
print(calculate_rows_of_lights(-19,-20))