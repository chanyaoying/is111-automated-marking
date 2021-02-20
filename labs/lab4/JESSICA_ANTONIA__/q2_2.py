def calculate_rows_of_lights(budget, cost_per_light):
    rows = 0
    total_cost = 0
    for i in range (1,100):
        if total_cost < budget:
            total_cost += i*cost_per_light
            rows = i - 1
    return rows

pass
pass
pass
