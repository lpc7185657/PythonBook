from random import randint
import pygal

class Die():
    """表示一个骰子的类"""
    def __init__(self,num_sides=6):
        self.num_sides = num_sides
    
    def roll(self):
        return randint(1,self.num_sides)

die1 = Die()
die2 = Die()
a = []
for roll in range(10000000):
    b = die1.roll() + die2.roll()
    a.append(b)

list1 = []
max_value = die1.num_sides + die2.num_sides
for value in range(2,max_value+1):
    num1 = a.count(value)
    list1.append(num1)

print(list1)

hist = pygal.Bar()
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
hist.add('D6',list1)
hist.render_to_file('die_visual.svg')