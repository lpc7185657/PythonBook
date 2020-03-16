""" #8-9
magic_name = ['Mason','Cristian','Emerson','Maximus']
def show_magicians(name):
    for a in name:
        print(a)
b = show_magicians(magic_name)

magic_name1 = ['Mason','Cristian','Emerson','Maximus']
new_name1 = []
def make_great(old_list,new_list):
    while old_list:
        a = old_list.pop()
        b = 'The great ' + a
        new_list.append(b)
def show_magicians1(name):
    for c in name:
        print(c)
make_great(magic_name1,new_name1)
show_magicians1(new_name1) """

magic_name1 = ['Mason','Cristian','Emerson','Maximus']
new_name1 = []

def make_great(old_list,new_list):
    while old_list:
        a = old_list.pop()
        b = 'The great ' + a
        new_list.append(b)

def show_magicians1(name):
    for c in name:
        print(c)
make_great(magic_name1[:],new_name1)
show_magicians1(new_name1)
show_magicians1(magic_name1)
print(magic_name1)
print(new_name1)