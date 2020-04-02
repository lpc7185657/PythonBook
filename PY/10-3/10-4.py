a = '请输入用户名：'
while True:
    c = input(a)
    b = r'PY\10-3\guest_book.txt'
    with open(b,'a') as guest:
        guest.write(c + '\n')
        print('你好！ ' + c)
    break