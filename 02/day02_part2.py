import pandas as pd

data = pd.read_csv("../inputs/AoC_Inputs.csv")
data = data.dropna()
depths = data.day01.tolist()
planned_course = data.day02.tolist()

depth = 0
horiz_pos = 0
aim = 0

for command in planned_course:
    [direction, unit_string] = command.split()
    units = int(unit_string)
    if direction == "forward":
        horiz_pos = horiz_pos + units
        depth = depth + (aim * units)
    elif direction == "up":
        aim = aim - units
    elif direction == "down":
        aim = aim + units


print(f"Final position: horiz_pos = {horiz_pos}, depth = {depth}")
print(f"Mutliplying the two gives: {horiz_pos*depth}")
