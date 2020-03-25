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

class ECar(Car):  #继承父类
    '''电动汽车的独特之处'''

    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()

my_tesla = ECar('tesla','model s','2016')
print(my_tesla.descriptive()) #打印名字

my_tesla.battery.discribe_battery() #查看实例中电瓶实例（属性）的电瓶容量
my_tesla.battery.get_range()
my_tesla.battery.battery_size = 85 #修改电瓶容量
my_tesla.battery.get_range()