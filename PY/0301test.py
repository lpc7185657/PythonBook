#5-8 #5-9
user_name = ['Zedd','Admin','lpc','Rbb','Skrillex']
if user_name:
    for b in user_name:
       if b == 'Admin':
           print('欢迎您，管理员。')
       else:
           print('欢迎您' + b + '，感谢您再次回来。')
else:
    print('没有您的用户名！')
#5-10
user_name1 = ['Zedd','Admin','lpc','Rbb','Skrillex']
user_name2 = ['Zedd','LPC','lpc','123','222','333']
for a in user_name2:
    if a.lower() in user_name1:
        print(a + '用户名已重复！')
    else:
        print(a + '用户名可以创建！')
#5-11
list = []
for a in range(1,10):
    list.append(a)
print(list)
for b in list:
    if b == 1:
        print("1st")
    elif b == 2:
        print('2nd')
    elif b == 3:
        print('3rd')
    else:
        print(str(b) + 'th')
