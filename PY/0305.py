alien1 = {'color':'green','points':'5'}
alien2 = {'color':'yellow','points':'10'}
alien3 = {'color':'red','points':'15'}
aliens = [alien1,alien2,alien3]
for a in aliens:
    print(a)
print('\n\n')

aline_30 = []
for num in range(30):
    new_alien = {'color':'green','points':'5','speed': 'slow'}
    aline_30.append(new_alien)
for new in aline_30[:5]:
    print(new)
print(str(len(aline_30)))
for new_1 in aline_30[0:3]:
    if new_1['color'] == 'green':
        new_1['color'] = 'yellow'
        new_1['points'] = '10'
        new_1['speed'] = 'medium'
    elif new_1['color'] == 'yellow':
        new_1['color'] = 'red'
        new_1['points'] = '15'
        new_1['speed'] = 'fast'
print('\n')
for new_aliens in aline_30:
    print(new_aliens)


pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
}
print('You ordered a ' + pizza['crust'] + '-crust pizza.')
for topping in pizza['toppings']:
    print('\t' + topping)

favorite_languages = {
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell']
}
for a,b in favorite_languages.items():
    print(a + '\'s favorite languages are:')
    for c in b:
        print('\t' + c)
    print('\n')
