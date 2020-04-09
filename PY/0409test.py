import json
#10-11 10-12
# num = 'numbers.json'
# try:
#     with open(num) as n1:
#         b = json.load(n1)
#     print('你输入的数字是' + b + '!')
# except FileNotFoundError:
#     a = input('输入一个你喜欢的数字：')
#     with open(num,'w') as n:
#         json.dump(a,n)

#10-13
def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def returnname():
    filename = 'username.json'
    with open(filename) as f_obj:
        a = json.load(f_obj)
        b = input(a + ' ,这是你的用户名吗？(yes/no)')
        if b == 'yes':
            return greet_user()
        elif b == 'no':
            return get_new_username()

def get_new_username():
    username = input('What is your name?')
    filename = 'username.json'
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
    return username

def greet_user():
    username = get_stored_username()
    print('Welecome back,' + username + '!')

returnname()
