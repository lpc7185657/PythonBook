a = r'PY\10-1\learn.txt'
with open(a) as txt:
    b = txt.read()
    print(b)
print('-------------------------------------')

with open(a) as txt:
    for c in txt:
        print(c)
print('-------------------------------------')

with open(a) as txt:
    d = txt.readlines()

e = ''
for f in d:
    e += f

print(e)