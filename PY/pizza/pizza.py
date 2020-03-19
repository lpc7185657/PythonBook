def make_pizza2(size,*toppings):
    print('\nMaking a pizza wish the following toppings:')
    print('-- ' + str(size))
    for a in toppings:
        print('- ' + a)