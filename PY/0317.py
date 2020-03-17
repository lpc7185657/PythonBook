#8.5
def make_pizza(*toppings):
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

def make_pizza1(*toppings):
    print('\nMaking a pizza wish the following toppings:')
    for a in toppings:
        print('- ' + a)
make_pizza1('pepperoni')
make_pizza1('mushrooms','green peppers','extra cheese')

#8.5.1
def make_pizza2(size,*toppings):
    print('\nMaking a pizza wish the following toppings:')
    print('-- ' + size)
    for a in toppings:
        print('- ' + a)

make_pizza2('pepperoni')
make_pizza2('mushrooms','green peppers','extra cheese')

#8.5.2
def build_profile(first,last,**user_info):
    profile = {}
    profile['First name'] = first
    profile['Last name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert','einstein',location = 'princeton',field = 'physics')
print(user_profile)