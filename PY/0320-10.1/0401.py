a = r'F:\Python\PY\0320-10.1\pi_million_digits.txt'
with open(a) as file_object:
    contents = file_object.readlines()
pi_string = ''
for line in contents:
    pi_string += line.strip()
print(pi_string[:52] + '...')
print(len(pi_string))

a = r'F:\Python\PY\0320-10.1\pi_million_digits.txt'
with open(a) as file_object:
    contents = file_object.readlines()
pi_string = ''
for line in contents:
    pi_string += line.strip()
birthday = input('输入你的生日：')
if birthday in pi_string:
    print('你的生日在圆周率里面！')
else:
    print('你的生日不在圆周率里面！')