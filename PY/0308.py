prompt = '输入：\n你喜欢去哪？'
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(city)