#9-6
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

class IceCreamStand(Restaurant):
    '''冰淇淋的店'''

    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['cool','hot','ice']
    
    def get_flavors(self):
        for a in self.flavors:
            print(a.title())
    
ice = IceCreamStand('冰激凌店','aa')
ice.get_flavors()


#9-7
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

class Admin(User):
    '''创建管理员用户'''

    def __init__(self,first_name,last_name,age):
        super().__init__(first_name,last_name,age)
        self.privileges = ['can add post','can delete post','can ban user']
    
    def show_privileges(self):
        for b in self.privileges:
            print(b)

ad = Admin('l','pc',29)
ad.describe_user()
ad.show_privileges()
#9-8
class Privileges():
    '''编辑权限类'''
    def __init__(self):
        self.privileges = ['can add post','can delete post','can ban user']
    
    def show_privileges(self):
        for b in self.privileges:
            print(b)

class Admin(User):
    '''创建管理员用户'''

    def __init__(self,first_name,last_name,age):
        super().__init__(first_name,last_name,age)
        self.privileges = Privileges()

adm = Admin('li','peng',22)
adm.privileges.show_privileges()

#9-9
class Car(): # 创建汽车类
    '''一次模拟汽车的简单尝试'''

    def __init__(self,make,model,year): #初始化属性
        self.make = make
        self.model = model
        self.year = year

    def descriptive(self): # 打印完整名字
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self): # 打印公里数
        print("This car has " + str(self.odometer_reading) + "miles on it.")

class Battery(): #新建电瓶类
    '''模拟电动车电瓶的简单尝试'''

    def __init__(self,battery_size=70):
        self.battery_size = battery_size

    def discribe_battery(self):
        '''打印电瓶容量信息'''
        print("This car has a " + str(self.battery_size) + "-kw battery.")

    def get_range(self):
        '''打印一条消息，指出电瓶续航里程'''
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        msg = 'This car can go approximately ' + str(range)
        msg += ' miles on a full charge.'
        print(msg)
    
    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85


class ECar(Car):  #继承父类
    '''电动汽车的独特之处'''

    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()

acc = ECar('tesla','model s','2016')
acc.battery.get_range()

acc.battery.upgrade_battery()
acc.battery.get_range()