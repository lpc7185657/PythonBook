name = ['jay','skrillex','avicii','zedd','tobu','lpc','rbb','diplo']
#3.3
print(name)
print(name[-1])
print(sorted(name,reverse=True,))
print(name[-1])
name.reverse()
print(name)

#4
for a in name:
    print(a + ',你真厉害！')

#4.2.5
for num in range(1,13):
    print(num)

b = list(range(2,20,2))
print(b)

c = []
for number in range(1,11):
    c.append(number**2)
print(c)