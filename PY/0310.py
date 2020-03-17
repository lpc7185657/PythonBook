namelist = {}
a = True
while a:
    b = input('你叫什么名字：')
    c = input('你最喜欢哪座山？')
    namelist[b] = c
    d = input('还有人需要调查吗？(yes or no)')
    if d == 'no':
        a = False
print('\n\n------现在显示调查结果------')
for e,f in namelist.items():
    print(e + '喜欢' + f + '。')