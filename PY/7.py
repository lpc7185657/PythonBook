# 逢7过游戏
a=1
while a<=100: #创建循环使a>100时停止
       if a%7==0 or a%10==7 or a//10==7: #创建数字包含7或7的条件
              pass
       else:
              print(a)
       a=a+1 # 每次循环使a+1
input("请按任意键退出")
