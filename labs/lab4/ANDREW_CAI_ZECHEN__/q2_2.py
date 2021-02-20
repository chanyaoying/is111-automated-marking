def calculate_rows_of_lights(budget,cost_per_light):
    num = budget / cost_per_light
    available = int(num)
    row = 0
    use = 0
    for i in range(available):
        row += 1
        use = (row * (row + 1)) / 2
        if use > available:
            row = row - 1
            break
    return row

print(calculate_rows_of_lights(50,2) == 6)
print(calculate_rows_of_lights(100,3) == 7)
print(calculate_rows_of_lights(10,12) == 0)