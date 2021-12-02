import pandas as pd

data = pd.read_csv("../inputs/AoC_Inputs.csv")
data = data.dropna()
depths = data.day01.tolist()
planned_course = data.day02.tolist()

#print(depths, planned_course)

depth = 0
horiz_pos = 0

for command in planned_course:
    [direction, unit_string] = command.split()
    units = int(unit_string)
    if direction == "forward":
        horiz_pos = horiz_pos + units
    elif direction == "up":
        depth = depth - units
    elif direction == "down":
        depth = depth + units


print(f"Final position: horiz_pos = {horiz_pos}, depth = {depth}")
print(f"Mutliplying the two gives: {horiz_pos*depth}")

# Final position: horiz_pos = 2034, depth = 702
# Mutliplying the two gives: 1427868