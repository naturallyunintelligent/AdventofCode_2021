import pandas
from pathlib import Path

#path = Path.home()/"Documents/Study/AdventofCode_2021/01/Day01/day1_input.csv"

#with path.open(mode='r') as inputcsv:
data = pandas.read_csv("day1_input.csv")
depths = data.Depths.tolist()
#print(depths)
count = 0
i = 0
for current_depth in depths[1:]:
    print(f"current_depth = {current_depth}m, previous datapoint was {depths[i]}units")
    if current_depth > depths[i]:
        count += 1
        print(f"depth increased, total increases: {count}")
    else:
        pass
    i += 1


print(f"Finished, total increases: {count}")
