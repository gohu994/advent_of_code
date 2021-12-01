import pandas as pd

x = pd.read_csv('input', sep="\t", header=None)

increases = 0

for i in range (len(x[0])-1):
    if x[0][i] < x[0][i+1] :
        increases += 1

print(increases)