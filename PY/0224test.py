#4-3
for num in range(1,21):
    print(num)

    

#4-4 4-5
a = list(range(1,1000001))
print(sum(a))

#4-6
b = list(range(1,21,2))
for num1 in b:
    print(num1)

#4-7
c = list(range(3,31,3))
for i in c:
    print(i)

#4-8
d = []
for num2 in range(1,11):
    d.append(num2**3)
for e in d:
    print(e)

#4-9
f =[num3**3 for num3 in range(1,11)]
print(f)