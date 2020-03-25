# P20 

price = input('How much did you pay?\n')
price = float(price)

if price >= 1:
    tax = .07
else:
    tax = 0
print('Tax rate is ' + str(tax))