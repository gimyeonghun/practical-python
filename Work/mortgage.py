# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
month = 0
payment = 2684.11
total_paid = 0.0

while principal > 0:
    month = month + 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    if month <= 12:
        principal = principal - 1000
        total_paid = total_paid + 1000
        
print('Total paid', total_paid, "over", month, "months")
