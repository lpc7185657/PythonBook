#name = ['jay','skrillex','avicii','zedd','tobu','lpc','rbb','diplo']
#a = name[:]
#print(name)
#a.append("123")
#print(a)

num = ['123','456','789']
num[0] = '000'
print(num)

name = ['jay','skrillex','avicii','zedd','tobu','lpc','rbb','diplo']
for i in name:
    if i == 'jay':
        print(i.title())
    else:
        print(i.upper())

#a = int(input('输入一个数字：'))
#while a == 23:
#    if a < 23:
#        b = input('这个数字比它大！请再输入一次：')
#        print(b)
 #   elif a > 23:
 #       c = input('这个数字比它小！请再输入一次：')
 #       print(c)
 #   else:
  #      d = '就是23！'
 #       print(d)

a = '20'
list = ['1','2','6','15','20','25','16','22']
if a in list:
    print('baohan')
else:
    print('bubaohan')