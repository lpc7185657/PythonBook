alien = {'color':'green','point': 5}
print(alien['color'])
print(alien['point'])
print('a' + str(alien['point']))
alien['x_position'] = 0 #外星人X轴位置
alien['y_position'] = 25 #外星人Y轴位置
print(alien)
alien['color'] = 'red'
print('现在外星人的颜色是：' + alien['color'] + '。\n\n')
alien['speed'] = 'medium' #外星人移动速度
print('Original x_position:  ' + str(alien['x_position']))
if alien['speed'] == 'low': #慢速移速为1
    x_increment = 1
elif alien['speed'] == 'medium': #中速移速为2
    x_increment = 2
else:
    x_increment = 3 #快速移速为3
alien['x_position'] = alien['x_position'] + x_increment #外星人移动格子数
print('New x_position:  ' + str(alien['x_position']))