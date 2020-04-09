import json

# filename = [1,2,3,4,5]
# a = 'numbers.json'
# with open(a,'w') as b:
#     json.dump(filename,b)

# with open(a) as f_obj:
#     numbers = json.load(f_obj)
# print(numbers)

# username = input('What is your name?')

#filename = 'username.json'
# with open(filename,'w') as f_obj:
#     json.dump(username,f_obj)
#     print('We\'ll remeber you when you come back,' + username + '!')

# with open(filename) as f_obj:
#     a = json.load(f_obj)
#     print(a)

# filename = 'username.json'
# try:
#     with open(filename) as f_obj:
#         username = json.load(f_obj)
# except FileNotFoundError:
#     username = input('What is your name?')
#     with open(filename,'w') as f_obj:
#         json.dump(username,f_obj)
#         print('We\'ll remeber you when you come back,' + username + '!')
# else:
#     print('Welecome back,' + username + '!')

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():
    username = get_stored_username()
    if username:
        print('Welecome back,' + username + '!')
    else:
        username = input('What is your name?')
        with open(filename,'w') as f_obj:
            json.dump(username,f_obj)
            print('We\'ll remeber you when you come back,' + username + '!')

greet_user()