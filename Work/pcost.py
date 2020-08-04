# pcost.py
#
# Exercise 1.27

import csv
import sys
import fileparse

def portfolio_cost(filename):
    tcost = 0.0
    data = fileparse.parse_csv(filename, types=[str, float, float])
    for row in data:
        tcost = tcost + (row['shares'] * row['price'])
    return tcost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)

print(f"Total cost {cost}")
       
