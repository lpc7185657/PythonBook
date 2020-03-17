a = int(input('请输入一个数字：'))
if a % 2 == 0:
    print('数字 ' + str(a) + ' 是偶数')
else:
    print('数字 ' + str(a) + ' 是基数')

name = '说一些话。'
name += '输入"quit"以退出程序。'
a = True
while a :
    message = input(name)
    if message != 'quit':
        print(message)
    else:
        a = False
