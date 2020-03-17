#7-8
sandwich_orders = ['Ham and egg sandwich','Egg sandwich','Bacon and cedars',
'Chicken sandwich','pastrami','pastrami','pastrami']
finished_sandwiches = []
while sandwich_orders:
    a = sandwich_orders.pop()
    finished_sandwiches.append(a)
    print('I made your ' + a + '.')
for i in finished_sandwiches:
    print(i)
#7-9
print('五香烟熏牛肉卖完了。')
while 'pastrami' in finished_sandwiches:
    finished_sandwiches.remove('pastrami')
for i1 in finished_sandwiches:
    print(i1)