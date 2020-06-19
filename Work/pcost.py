# pcost.py
#
# Exercise 1.27



def portfolio_cost(filename):
    tcost = 0.0
    with open(filename, 'rt') as f:
        headers = next(f).split(',')
        for line in f:
            row = line.split(',')
            print(tcost)
            tcost = tcost + (float(row[1]) * float(row[2]))
    return tcost



cost = portfolio_cost('Data/portfolio.csv')

print(f"Total cost {cost}")
       
