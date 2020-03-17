#8.3.1
def full_name(first_name,last_name):
    '''返回整洁的名字'''
    name = first_name + ' ' + last_name
    return name.title()
    
get_name = full_name('li','pengcheng')
print(get_name)

#8.3.2
def full_name1(first_name,last_name,middle_name=''):
    if middle_name:
        name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        name = first_name + ' ' + last_name 
    return name.title()

my_name = full_name1('jimi','hendrix')
print(my_name)
my_name = full_name1('john','hooker','lee')
print(my_name)

#8.3.3
def a(first_name,last_name):
    name = {'first' : first_name,'last' : last_name}
    return name
b = a('li','pengcheng')
for c in b.values():
    print(c)

#8.3.4
def build_person(first_name,last_name,age = ''):
    a = {'first' : first_name,'last' : last_name}
    if age:
        a['age'] = age
    return a
b = build_person('li','pengcheng',27)
print(b)

b = build_person('li','pengcheng')
print(b)