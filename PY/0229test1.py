#5-3 5-4 5-5
#color = input('输入颜色：')
#if color == 'green':
#    a = 5
#elif color == 'yellow':
#    a = 10
#else:
 #   a = 15
#print('获得了' + str(a) + '点!')

# 5-6
age = int(input('请输入你的年龄：'))
if age < 2:
    print('他是婴儿。')
elif age < 4:
    print('他正在蹒跚学步。')
elif age < 13:
    print('他是儿童。')
elif age < 20:
    print('他是青少年。')
elif age < 65:
    print('他是成年人。')
else:
    print('他是老年人。')
