# pcost.py
#
# Exercise 1.27
import csv
import sys
def portfolio_cost(filename):
    price = 0.0
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            price += int(row[1]) * float(row[2])
            
        return price

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
    
price = portfolio_cost(filename)    
print(f'Total cost {price: 0.2f}')
    
    
