def market(prise, discount):
    calculation = lambda prise, discount: prise - discount
    return calculation

result = market(150, 8.50)
print(result)