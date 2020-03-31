a = r'F:\Python\PY\0320-10.1\123\pi_digits.txt'
with open(a) as file_object:
    contents = file_object.read()
    print(contents.rstrip())



a = 'pi_digits.txt'
with open(a) as file_object:
    for line in file_object:
        print(line.rstrip())

a = 'pi_digits.txt'
with open(a) as file_object:
    line = file_object.readlines()
for b in line:
    print(b.rstrip())


a = 'pi_digits.txt'
with open(a) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

