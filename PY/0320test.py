class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.asd = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.asd.title() + '餐厅')

    def open_restaurant(self):
        print(self.asd.title() + '餐厅开业啦！')

my_rest = Restaurant('aa','bb',)
print(my_rest.asd.title())
print(my_rest.cuisine_type.title())

my_rest.describe_restaurant()
my_rest.open_restaurant()


#9-3
class User():
    '''创建用户'''

    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def describe_user(self):
        print('New User:')
        print('Name: ' + self.first_name.title() + ' ' + self.last_name.title())
        print('Age: ' + str(self.age))

    def greet_user(self):
        print('Hello! ' + self.first_name.title() + ' '
        + self.last_name.title() + '.')

a = User('li','pengcheng',29)
a.describe_user()
a.greet_user()