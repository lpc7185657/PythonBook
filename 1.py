import os
x = os.listdir('F:\\迅雷')
list_item = []
for item in x:
    a = item.lower()
    if 'word' in a:
        list_item.append(a)
print(len(list_item),list_item)
aa = ''.join(list_item)
print(aa.count('word'))
