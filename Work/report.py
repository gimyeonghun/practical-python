# report.py
import csv
import fileparse

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    portfolio = []
    portfolio = fileparse.parse_csv(filename, types=[str, int, float])
    return portfolio

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    prices = fileparse.parse_csv(filename, types=[str, float], has_headers=False)
    return dict(prices)

def make_report_data(portfolio, prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows
        
# Read data files and create the report data        

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

# Generate the report data

report = make_report_data(portfolio, prices)

# Output the report
headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * len(headers))
for row in report:
    print('%10s %10d %10.2f %10.2f' % row)
