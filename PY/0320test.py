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
