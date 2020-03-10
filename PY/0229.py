age = 18
if age >= 18:
    print('大于18')
else:
    print('小于等于18')

a = int(input('请输入你的年龄：'))
if a < 4:
    b = 0
elif a >= 4 and a < 18:
    b = 5
elif a > 65:
    b = 5
else:
    b = 10
print('收费' + str(b) +'元。')
    