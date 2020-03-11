a = 0
while a < 11:
    a += 1
    if a % 2 == 0:
        continue
    print(a)

#7.3.1
name = ['jay','skrillex','avicii','zedd','tobu','lpc','rbb','diplo']
user_name = []
while name:
    name_append =  name.pop()
    user_name.append(name_append)
    print(name_append.title() + '已添加至验证用户。')
print('已验证用户有：')
for a in user_name:
    print(a)


name = ['jay','jay','jay','jay','skrillex','avicii','zedd','zedd',
'zedd','zedd','tobu','lpc','rbb','diplo']
while 'jay' in name :
    name.remove('jay')
while 'zedd' in name :
    name.remove('zedd')
print(name)