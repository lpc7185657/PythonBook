#7-4
a = '请输入要添加的食材，有“芝士”、“胡椒”、“牛肉”可选。输入quit退出。'
while True:
    b = input(a)
    if b == '芝士':
        print('我们将添加：' + b + '。')
    elif b == '胡椒':
        print('我们将添加：' + b + '。')
    elif b == '牛肉':
        print('我们将添加：' + b + '。')
    elif b == 'quit':
        print('程序已退出。')
        break
    elif b != '牛肉' or '芝士' or '胡椒':
        print('输入错误！')
#7-5
a = '请输入年龄：'
while True:
    b = int(input(a))
    if b < 3:
        c = '0'
    elif b >= 3 and b < 12:
        c = '10'
    else:
        c = '15'
    print('票价为：' + c + '元。')