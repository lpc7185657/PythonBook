class Car(): # 创建汽车类
    '''一次模拟汽车的简单尝试'''
    def __init__(self,make,model,year): #初始化属性
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def descriptive(self): # 打印完整名字
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self): # 打印公里数
        print("This car has " + str(self.odometer_reading) + "miles on it.")
    
    def update_odometer(self,mileage): # 增加指定公里数
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('error')
    
    def increment_odometer(self,miles): # 增加指定公里数
        self.odometer_reading += miles

class ElectricCar(Car): #创建子类电动汽车
    '''电动汽车的独特之处'''
    def __init__(self,make,model,year):
        super().__init__(make,model,year)#继承父类属性

my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.descriptive())

class ECar(Car): 
    '''电动汽车的独特之处'''
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size = 70
    
    def read_battery(self):
        print('这辆车电瓶容量：' + str(self.battery_size))

my_tesla11 = ECar('tesla','model s',2016)
my_tesla11.read_battery()