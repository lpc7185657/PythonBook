'''一组用于表示燃油汽车和电动汽车的类'''

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
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self,mileage): # 增加指定公里数
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('error')

    def increment_odometer(self,miles): # 增加指定公里数 （测试重写父类）
        self.odometer_reading += miles

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