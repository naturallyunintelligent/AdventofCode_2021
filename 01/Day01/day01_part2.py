import pandas

data = pandas.read_csv("day1_input.csv")
depths = data.Depths.tolist()

count = 0
prev_window_start = 0
previous_window = depths[prev_window_start] + depths[prev_window_start + 1] + depths[prev_window_start + 2]

for current_depth in depths[3:]:
    sliding_window = depths[prev_window_start+1] + depths[prev_window_start + 2] + current_depth
    print(f"current sliding window total = {sliding_window}m"
          f"previous window was {previous_window}")
    if sliding_window > previous_window:
        count += 1
        print(f"sliding window depth increased, total increases: {count}")
    else:
        pass
    previous_window = sliding_window
    prev_window_start += 1


print(f"Finished, total increases: {count}")
