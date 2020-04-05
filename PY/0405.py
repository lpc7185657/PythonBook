# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("不能除以0！")
# print(1+2)


# #10.3.3
# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")

# while True:
#     first_number = input('\nFirst number:')
#     if first_number == 'q':
#         break
#     second_number = input('\nSecond number:')
#     if second_number == 'q':
#         break

#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print('不可以除以0！')
#     else:
#         print(answer)

# #10.3.5
# file_name = r'PY\alice.txt'
# try:
#     with open(file_name) as f_obj:
#         contents = f_obj.read()
# except FileNotFoundError:
#     print('Sorry,the file: ' + file_name + ' does not exist.')
# else:
#     #计算文件有多少个单词
#     words = contents.split()
#     num_words = len(words)
#     print(num_words)

#10.3.7
def count_words(file_name):
    try:
        with open(file_name) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print('Sorry,the file: ' + file_name + ' does not exist.')
    else:
        #计算文件有多少个单词
        words = contents.split()
        num_words = len(words)
        print(num_words)

name = r'PY\alice.txt'
count_words(name)