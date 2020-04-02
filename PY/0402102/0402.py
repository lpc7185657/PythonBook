a = r'PY\0402102\123.txt'
with open(a,'w') as file_123:
    file_123.write('I love programming\n')
    file_123.write('I love programming\n')
    file_123.write('I love programming\n')
    file_123.write('I love programming\n')

a = r'PY\0402102\123.txt'
with open(a,'a') as file_123:
    file_123.write('I also lobe finding meaning in large datasets\n')
    file_123.write('I love creating apps that can run in a brower')