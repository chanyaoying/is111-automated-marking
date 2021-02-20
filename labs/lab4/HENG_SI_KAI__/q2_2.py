def calculate_rows_of_lights(budget, cost_per_light):
    rows_of_lights = 0
    no_of_lights = budget // cost_per_light
    while no_of_lights > 0:
        no_of_lights -= (rows_of_lights + 1)
        if no_of_lights < 0:
            break
        rows_of_lights += 1
    return rows_of_lights

print(calculate_rows_of_lights(50,2) == 6)
print(calculate_rows_of_lights(100,3) == 7)
print(calculate_rows_of_lights(10,12) == 0)

# enable the following lines of code to print the Christmas tree :)

# input_budget = int(input('Enter your budget: '))
# input_cost = int(input('Enter the cost per light: '))

# rows = calculate_rows_of_lights(input_budget,input_cost)
# for i in range(calculate_rows_of_lights(input_budget,input_cost)):
#     print(' ' * (rows-1) + '* ' * (i+1))
#     rows -= 1