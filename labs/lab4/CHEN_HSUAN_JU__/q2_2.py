def calculate_rows_of_lights(budget,cost_per_light):
    num_lights = budget // cost_per_light
    if budget < cost_per_light:
        row = 0
        return row
    if budget >= cost_per_light:
        row = []
        for i in range(1,num_lights):
            row.append(i)
            if sum(row) > num_lights:
                break
        row.pop()
        return row[-1] #return last element from the list

