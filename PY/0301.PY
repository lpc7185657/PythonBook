pizza = ['mushrooms','green peppers','exera cheese']
for a in pizza:
    
    if a =='green peppers':
        print('Sorry,we are out of green peppers right now.')
    else:
        print('Adding ' + a + '.')
print('\nFinished making your pizza!')

pizza = []
if pizza:
    for b in pizza:
        print('Adding ' + b + '.')
else:
    print('Are you sure you want a plain pizza?')


pizza = ('mushrooms','green peppers','extra cheese')
guke = ['mushrooms','french fries','extra cheese']
for c in guke:
    if c in pizza:
        print('Adding ' + c + '.')
    else:
        print('Sorry we don\'t have ' + c + '.')
print('\nFinished making your pizza!')

