# pcost.py
#
# Exercise 1.27

import csv

def portfolio_cost(filename):
    tcost = 0.0
    with open(filename, 'rt') as f:
        f = csv.reader(f)
        headers = next(f)
        for row in f:
            tcost = tcost + (float(row[1]) * float(row[2]))
    return tcost



cost = portfolio_cost('Data/portfolio.csv')

print(f"Total cost {cost}")
       
