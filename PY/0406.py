#10-6
# a = input('输入第一个数字：')
# b = input('输入第二个数字：')
# try:
#     num = int(a) + int(b)
# except ValueError:
#     print('输入错误!!')
# else:
#     print(num)

#10-7
# a = '输入第一个数字：'
# b = '输入第二个数字：'
# while True:
#     num1 = input(a)
#     num2 = input(b)
#     try:
#         num = int(num1) + int(num2)
#     except ValueError:
#         print('输入错误!!')
#     else:
#         print(num) 

#10-8
# a = 'C:/Users/Administrator/Desktop/cat.txt'
# b = 'C:/Users/Administrator/Desktop/dog.txt'
# c = 'C:/Users/Administrator/Desktop/ss.txt'
# def book(name):
#     try:
#         with open(name) as bookname:
#             readbook = bookname.read()
#     except FileNotFoundError:
#         print('没有找到' + name + '!请检查文件名。')
#     else:
#         print(readbook)

# book(a)
# book(b)
# book(c)

#10-9
# a = 'C:/Users/Administrator/Desktop/cat.txt'
# b = 'C:/Users/Administrator/Desktop/dog.txt'
# c = 'C:/Users/Administrator/Desktop/ss.txt'
# def book(name):
#     try:
#         with open(name) as bookname:
#             readbook = bookname.read()
#     except FileNotFoundError:
#         pass
#     else:
#         print(readbook)

# book(a)
# book(b)
# book(c)

#10-10
little_women = 'C:/Users/Administrator/Desktop/《Python》yandaimawenjian/chapter_10/little_women.txt'
def bookcount(word):
    with open(little_women) as book:
        a = book.read()
        c = word.lower()
        b = a.lower().count(c)
        print(b)

bookcount('Women')