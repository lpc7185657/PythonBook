class Car():
    '''创建一辆小汽车'''

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 20000 #设置默认公里数为0
    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self,mileage): #通过方法添加参数mileage，并关联到公里数属性
        '''
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
            print('This car has ' + str(self.odometer_reading) + ' miles on it.')
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self,miles): #通过增量记录公里数
        '''将里程表增加指定的量'''
        if miles >= 0:
            self.odometer_reading += miles
            print('This car has ' + str(self.odometer_reading) + ' miles on it.')
        else:
            print('error!')
        

my_new_car = Car('audi','a4','2016')

print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23 #修改公里数为23
my_new_car.read_odometer()

my_new_car.update_odometer(245)

my_new_car.increment_odometer(25000)

my_new_car.increment_odometer(-25000)