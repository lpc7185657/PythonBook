name = ['jay','skrillex','avicii','zedd','tobu']
a = "\n\t赴约名单为：" + ','.join(name) + "."
print(a.title())
dead = 'avicii'
name[2] = 'rezz'
print('\n\t"avicii"由于去世未能参加晚宴，且Rezz参加晚宴，重新发布赴约名单。')
b = "\n\t赴约名单为：" + ','.join(name) + "."
print(b)
print('\n\t主办方找到一张更大的餐桌，可以多容纳3个人！')
print('\n\tDiplo参加了晚宴！')
name.insert(0,'diplo')
c = "\n\t赴约名单为：" + ','.join(name) + "."
print(c)
print('\n\tlpc参加了晚宴！')
name.insert(3,'lpc')
d = "\n\t赴约名单为：" + ','.join(name) + "."
print(d.title())
print('\n\trbb参加了晚宴！')
name.append('rbb')
e = "\n\t赴约名单为：" + ','.join(name) + "."
print(e.title())

name.remove('diplo')
print("\n\t很抱歉，由于其他原因，Diplo不能参加晚宴。")
print("\n\t赴约名单为：" + ','.join(name) + ".")

name.remove('jay')
print("\n\t很抱歉，由于其他原因，jay不能参加晚宴。")
print("\n\t赴约名单为：" + ','.join(name) + ".")

name.remove('skrillex')
print("\n\t很抱歉，由于其他原因，Skrillex不能参加晚宴。")
print("\n\t赴约名单为：" + ','.join(name) + ".")

name.remove('rezz')
print("\n\t很抱歉，由于其他原因，Rezz不能参加晚宴。")
print("\n\t赴约名单为：" + ','.join(name) + ".")

name.remove('zedd')
print("\n\t很抱歉，由于其他原因，Zedd不能参加晚宴。")
print("\n\t赴约名单为：" + ','.join(name) + ".")

name.remove('tobu')
print("\n\t很抱歉，由于其他原因，Tobu不能参加晚宴。")
print("\n\t赴约名单为：" + ','.join(name) + ".")
del name[0]
del name[0]
print("\n\t赴约名单为：" + ','.join(name))