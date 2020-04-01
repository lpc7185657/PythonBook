a = r'PY\10-2\learn.txt'
with open(a) as txt:
    b = txt.readlines()

string = ''
for c in b:
    string += c
print(string.rstrip().replace('Python','C'))