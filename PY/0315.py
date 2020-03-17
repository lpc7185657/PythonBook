""" def get_formatted_name(first_name,last_name):
    '''返回整洁的姓名'''
    full_name = first_name + ' ' + last_name
    return full_name.title()
while True:
    print('Please enter your name.')
    print('enter "q" at any time to quit.')
    f_name = input('Your first name:')
    if f_name == 'q':
        print('exit.')
        break
    l_name = input('Your last name:')
    if l_name == 'q':
        print('exit.')
        break
    name = get_formatted_name(f_name,l_name)
    print('hello,',name,'!')
    break """

#8.4
def greet_name(name):
    for a in name:
        msg = 'hello ' + a + '!'
        print(msg)

b = ['lpc','zedd','skrillex']
greet_name(b)

#8-5
dayin = ['aaa','vbb','xxx','ccc']
liebiao = []
while dayin:
    a = dayin.pop()
    print('打印' + a)
    liebiao.append(a)
print(liebiao)

def print_models(unprinted,completed):
    while unprinted:
        b = unprinted.pop()
        print('打印：' + b)
        completed.append(b)
dayin = ['aaa','vbb','xxx','ccc']
liebiao = []
print_models(dayin[:],liebiao)
print(liebiao)
print(dayin)