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
    
    def increment_odometer(self,miles): # 增加指定公里数 （测试重写父类）
        self.odometer_reading += miles

class Battery():
    '''一次模拟电动汽车电瓶的简单尝试'''
    def __init__(self,battery_size=70):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kw battery.")
        
class ECar(Car): 
    '''电动汽车的独特之处'''
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size = 70   #添加子类独特的属性
    
    def read_battery(self):
        print('这辆车电瓶容量：' + str(self.battery_size))