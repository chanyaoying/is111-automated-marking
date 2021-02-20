def calculate_rows_of_lights(budget, cost_per_light):
    rows = 0
    total_cost = 0
    for i in range (1,100):
        if total_cost < budget:
            total_cost += i*cost_per_light
            rows = i - 1
    return rows

print(calculate_rows_of_lights(50,2) == 6)
print(calculate_rows_of_lights(100,3) == 7)
print(calculate_rows_of_lights(10,12) == 0)