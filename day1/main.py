import pandas as pd

x = pd.read_csv('input', sep="\t", header=None)

# part 1
increases = 0

for i in range (len(x[0])-1):
    if x[0][i] < x[0][i+1] :
        increases += 1

print("PART ONE : ", increases, "increases")

# part 2
increased_windows = 0

new_window = 1000
for i in range(1,len(x[0])-1):
    if x[0][i-1] + x[0][i] + x[0][i+1] > new_window:
        increased_windows += 1
    new_window = x[0][i-1] + x[0][i] + x[0][i+1]
    # print(x[0][i-1], x[0][i], x[0][i+1], " new window : ", new_window)

print("PART TWO : ", increased_windows, "increased windows")