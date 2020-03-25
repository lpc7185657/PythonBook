class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.asd = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.asd.title() + '餐厅')

    def open_restaurant(self):
        print(self.asd.title() + '餐厅开业啦！')
    
    def a(self,b):
        self.number_served = b
        print('我们有 ' + str(b) + ' 人在本餐馆就餐过！')
    
    def read(self):
        print('这家店每天可以就餐的人数为：' + str(self.number_served))

    def increment_number_served(self,c):
        self.number_served += c

my_rest = Restaurant('aa','bb',)
print(my_rest.asd.title())
print(my_rest.cuisine_type.title())

my_rest.describe_restaurant()
my_rest.open_restaurant()

my_rest.a(25)

my_rest.increment_number_served(200)
my_rest.read()


#9-3
class User():
    '''创建用户'''

    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0
    
    def describe_user(self):
        print('New User:')
        print('Name: ' + self.first_name.title() + ' ' + self.last_name.title())
        print('Age: ' + str(self.age))

    def greet_user(self):
        print('Hello! ' + self.first_name.title() + ' '
        + self.last_name.title() + '.')

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(str(self.login_attempts))
    
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(str(self.login_attempts))


a = User('li','pengcheng',29)
a.describe_user()
a.greet_user()
a.increment_login_attempts()
a.increment_login_attempts()
a.increment_login_attempts()
a.increment_login_attempts()
a.increment_login_attempts()
a.reset_login_attempts()