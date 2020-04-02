a = input('请输入你的名字：')
b = r'PY\10-3\guest.txt'
with open(b,'a') as guest:
    guest.write(a + '\n')

