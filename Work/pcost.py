# pcost.py
#
# Exercise 1.27

import csv,sys

def portfolio_cost(filename):
    tcost = 0.0
    with open(filename, 'rt') as f:
        f = csv.reader(f)
        headers = next(f)
        for row in f:
            tcost = tcost + (float(row[1]) * float(row[2]))
    return tcost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)

print(f"Total cost {cost}")
       
