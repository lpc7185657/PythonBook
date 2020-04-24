import matplotlib.pyplot as plt
from random import choice

#15.2
# squares = [1,4,9,16,25]
# input_values = [1,2,3,4,5]
# plt.plot(input_values,squares,linewidth=5)
# plt.title('Square Numbers',fontsize = 24)
# plt.xlabel('Value',fontsize = 14)
# plt.ylabel('Square of Value',fontsize = 14)
# plt.tick_params(axis='both',labelsize = 20)
# plt.show()

#15.2.3
# plt.scatter(2,4,s=20)
# plt.title('Square Numbers',fontsize = 24)
# plt.xlabel('Value',fontsize = 14)
# plt.ylabel('Square of Value',fontsize = 14)
# plt.tick_params(axis='both',labelsize = 20,which='major')
# plt.show()

#15.2.4
# x_values = [1,2,3,4,5]
# y_values = [1,4,9,16,25]
# plt.scatter(x_values,y_values,s=200)
# plt.show()

#15.2.5
# x_values = list(range(1,10001))
# y_values = [x**2 for x in x_values]
# plt.scatter(x_values,y_values,c=x_values,cmap=plt.cm.Blues,s=2)
# plt.show()

#15.3.1
class RandomWalk():
    '''生成一个随机漫步数据的类'''
    def __init__(self,num_points=50000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        '''随机漫步包含的所有点'''
        while len(self.x_values) < self.num_points:
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance
            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

rw = RandomWalk()
rw.fill_walk()
point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.cividis,s=1)
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.show()