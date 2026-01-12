order1 ='----Orders----'
order2 = 'PIZZA: 1.25$ PER SLICE;'
order3 ='SANDWICH:2$'
order4 = 'JUICE:1.5$ (PEACH)'
orderend = '----End Orders----'

orderlist = [
'sandwich','juice','pizza',
'SANDWICH','JUICE','PIZZA'
]

print(order1)
print(order2)
print(order3)
print(order4)
print(orderend)

order = input("\nYour order:")

if not order in orderlist:
    print("no specific order available")
else:
    print("bought succesfully "+order.lower())