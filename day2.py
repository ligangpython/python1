
#2
# a = int (input("输入第一个同学成绩："))
# b = int (input("输入第二个同学成绩："))
# c = int (input("输入第三个同学成绩："))

#取最小
# d = a if a < b else b 
# e = d if d < c else c
#最大
# d = a if a > b else b 
# e = d if d > c else c

# if a < b:
#     e = a
# else:
#     e = b
# if e < c
#     print("最低成绩为：",e)
# else:
    # print("最低成绩为：",c)


# e = max(a,b,c)
# f = min(a,b,c)
# print(e)
# print(f)



# a = int(input("输入体重："))
# b = int(input("输入身高："))

# BIM = a/b**2

# if BIM < 18.5:
#     print("体重太轻")
# if 18.5 <= BIM < 24:
#     print("正好")
# if BIM > 24:
#     print("过重")



# print(1,2,3)


# a = int (input("请输入宽度：") or 0)
# b = a * "#"
# print(b)
# print('#' + (a-2)*' ' + '#')
# print('#' + (a-2)*' ' + '#')
# print(b)



# s = 'wertyiokwdc'
# a = len(s)
# print(a)
# if a % 2 == 1:
#     b = a // 2 
#     print(s[b])


# s = input("输入字符串：")

# a = len(s)

# print(s[1:a-1])

#2

# s = input("输入字符串：")
# b = len(s)
# a = s[0:b//2]
# c = s[-1:-((b//2)+1):-1]

# print(a)
# print(c)
# if a == c :
#     print("回文")
# else:
#     print("不是回文")


# s = input("输入字符串：") or None
# print (ord(s[0]))

# s = int(input("输入数字："))
# print(chr(s))





#1
# s = input("请输入字符串：")

# print(s.count(" "))
# print(s.strip())
# a = len(s.strip())
# print(a)
# c = s.isdigit()
# print(s.isdigit())

# if c == True:
#     if int(s) > 100:
#         print("大于１００")
#     else:
#         print("小于１００")

# s = input("请输入字符串：")
# a = '+' + '-'*20 + 'l+'
# print(a) 

# print('|',s.center(18),'|')


#此处有问题　　　　１８



# a = input("输入字符串１：")
# b = input("输入字符串２：")
# c = input("输入字符串３：")

# print("%20s\n" % a,"%20s\n" % b,"%20s\n" % c,sep = '')
# print("%20s" % a)
# print("%20s" % b)
# print("%20s" % c)



# a = int(input("输入数字："))
# b = 0
# while a >=b:
#     print("这是第",b,"行")
#     b += 1



# i = 1
# while i <= 10:
#     print("这是１行文字")
#     i += 1
#     print("程序结束")
    


#1

# s = input("输入字符串：")
# i = 0

# while i < len(s) - 1:
#     b = ord(s[i])
#     c = ord(s[i+1])
#     i += 1
#     if c > b:
#         e = c
#     else:
#         e = b
# f = chr(e)
# print(f)
  

# i = 1
# while i <= 20:
#     print(i,end = ' ')
#     i += 1
    

# i = 10
# while i > 0:
#     print(i)
#     i -= 1
    

# i = 1
# while i < 21:
#     if i < 6:
#         print(i,end = ' ')
    
#     if 6 <= i < 11:
#         if i == 6:
#             print()
#         print(i,end = ' ')
#     if 11 <= i < 16:
#         if i == 11:
#             print()
#         print(i,end = ' ')
#     if 16 <= i < 21:
#         if i == 16:
#             print()
#         print(i,end = ' ')
#     i += 1
# else:
#     pass

# 思路：先将所有的输出，然后再将其断开


# a = int (input("请输入整数："))
# print("@"*a)
# i = 1
# while i < a-1:
#     print("@","@",sep = ' '*(a - 2))
#     i += 1
#     if i == a-1:
#     print("@"*a)


# a = int (input("请输入整数：")) 
# j = 0
# while j < a:

#     i = 0 
#     while i < a:
#         print(i+1,end = " ")
#         i += 1
#     else:
#         print()
#     j += 1
# else:
#     pass

   
#

# a = int(input("请输入整数："))
# i = 1
# s = 0
# while i <= a:
#     s = s + i
#     i += 1
# print(s)



# a = 3.223456
# print("%.6d" % a)   

#1
#任意输入一些数，当输入负数时结束输入
#当输入完成后，打印您输入的这些数的和
# a = 0
# s = 0
# while a >= 0:
#     a = int(input("请输入数据："))
#     s = s + a
   
#     if a < 0:
#         break
#         print("结束输入。")
# print(s)



#2
#求sn = 1 + 1/2 + 1/4 + 1/8 +....1/(2**n)

# a = int(input("请输入数据："))
# i = 0
# sn = 0
# while i < a:
#     sn = sn + 1/(2**i)
#     i += 1
#     sn = round(sn,100)
# print(sn)

#3
#打印*型三角形
# a = int(input("请输入数据："))

# i = 0
# while i < a:
#     s = "*"*(i + 1)
#     i += 1
#     # print(s)

#     print("%s" % s)


# while i < a:
#     s = "*"*(a - i)
#     i += 1
#     # print(s)
#     r = "%%%ds" % a
#     print(r % s)

#########################################


                   #day5


########################################

# s = "ddskeid"

# for ch in s:
#     print("ch======>",ch)
#在此处有一个赋值操作，依次从s中拿出d,d,s等字符
#然后将其赋值给ch


#2
# s = input("请输入字符串：")
# i = 0
# j = 0
# count_space = 0
# #方法１

# for ch in s:
#     if ch == 'A':
#         i += 1
#     if ch == ' ':
#         j += 1
# print('A的个数为：',i,'空格的个数为：',j)

#方法２
# i = s.count(" ")
# j = s.count("A")
# print('A的个数为：',i,'空格的个数为：',j)

#方法３

# while i < len(s):
#     if s[i] =='A':
#         j += 1
#     if s[i] == " ":
#         count_space += 1
#     i += 1
# print("A的个数为：",j,"空格的个数为：",count_space)
   


# s = 'ABCD'
# for c in s:
#     if c == 'D':
#         break
# else:
#     print("for不能提到可迭代对象而结束。",D)



#for 打印　１－２０
# for a in range(21,0,-1):
#     print(a,end = ' ')
# print()


#100以内有哪些整数和自身＋１的乘积在对１１求余的结果等于８？
# for x in range(100):
#     if x * (x+1) % 11 == 8:
#         print(x)



# 1+3+5+7+....９９的和

# sum = 0
# for x in range(1,100,2):
#     sum += x
# print(sum)

#方法２
# i = 1 
# sum = 0
# while i < 100:
#     sum += i
#     i += 2
# print(sum)
   

#用ｗｈｉｌｅ打印　１　３　５　７　。。。１９　一行

# i = 1
# while i < 20:
#     print(i,end = ' ')
#     i += 2

# for x in range(1,20,2):
#     print(x,end = " ")
    


#ｐｒｉｎｔ执行多少次

# i = 0
# for x in range(5):
#     for y in range(10):
#         i += 1
#         print(x,y,'ABC')
# print("循环次数为：",i)
        

#用ｆｏｒ实现：输入一个数Ｗ代表正方形的宽度，打印正方形
# w = int(input("请输入宽度："))
# i = 0 
# j = 0 
# while j < w :
    
#     for wigth in range(1,w+1,1):
#         print(wigth,end = ' ')
#         i += 1
#         if i % w == 0:
#             print()     
#     j += 1


#2

# for x in range(1,w + 1,1):
#     for y in range(x,w+x,1):
#         print("%2d" % y,end = " ")
#     print()
       

#＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃很重要      


#练习
#输入一个整数用ｂｅｇｉｎ绑定，再输入一个整数用end绑定
# 打印从ｂｅｇｉｎ开始，到end结束内的全部奇数（不包含end)

# begin = int(input("第一个数："))
# end = int(input("第二个数："))

# for x in range(begin,end):
#     if x % 2 ==0:
#         continue
#     print(x)

# i = 0
# y = begin - 1
# while i < (end - begin):
#     y += 1
#     i += 1
#     if (y-1) % 2 == 1:
#         continue
#     print(y)
    

#求１－１００之间所有不被　５　　７　　11整除的数的和

# sum = 0
# for x in range(1,101):
#     if x % 5 == 0 or x % 7 == 0 or x % 11 ==0:
#         continue
#     sum += x
# print(sum)


#将输入的三行文字，保存于一个列表Ｌ中，并打印。

# a = list (input("请输入第一行文字："))
# b = list (input("请输入第二行文字："))
# c = list (input("请输入第三行文字："))
# L= [a,b,c]
# print(L)
# l = a + b + c
# print(l)


#练习题
#１．输入任意行文字，存于列表Ｌ中，当不输入任何内容直接回车后结束输入
#　　　　１）打印Ｌ列表中的内容
#    ２）计算您共输入了几行
#    ３）计算你共输入了多少个字符


# i = 0
# L = []
# s = " "
# while s != '':
#     s = input("请输入文字：")
    
    # m = list(s)
#     L = L + m
#     i += 1

# print(L)
# print("共输入了","%d" % (i - 1),"行")
# marry = len(L)
# print("共输入了","%d" % marry,"个字符")



#2　输入一个整数（代表树干的高度）
#  打印出如下的一棵树
# 　　输入：２

# 　　　　　*
#     ***
#      *
#      *
     # 输入３　
      #   *
      #  ***
      # *****
      #   *
      #   *
      #   *

# a = int(input("请输入树的高度："))

# for l in range(1,2*a,2):
#     s = "*" * l
#     b = s.center(2*a - 1)
#     print(b)

# m = "*"
# d = m.center(2*a - 1)
# for y in range(1,a+1):
#     print(d)





#写一个程序，任意输入一个整数，判断这个数是否是素数（ｐｒｉｍｅ）
#素数:是只能被１和自身整除的正整数：
#如: 2  3 5 7 11等
#提示：用排除法：当判断X是否为素数时，只有让Ｘ分别除以：
#２，３，４，５．。。。。x-1
#只要整除了，那Ｘ不是素数，否则 x　是素数

# i = 0
# a = int (input("输入数字："))
# for x in range(2,a):
#     if a % x == 0:
#         print("不是素数")        
#     else:
#         i += 1
#         if i == a-2:   #注意是a - 多少    
#             print("是素数")
        
        
    



#４．算出１００　－１０００以内的水仙花数
#水仙花数是指百位的３次方　加上十位的３次方　加上个位的３次方等于原数的数

#如：
#１５３　＝　１**３　＋　５**３　＋　３**３
#答案:   153,370...


# for x in range(100,1000):
#     a = x // 100
#     b = x % 100 // 10
#     c = x % 100 % 10
#     if x == a ** 3 + b**3 + c**3:
#         print(x)
        

#方法２　列表 或者　字符串　做
# for x in range(100,1000):
#     l = str(x)    
#     if int(l[0]) ** 3 + int(l[1]) ** 3 + int(l[2]) ** 3 == x:
#         print(x)
        

#方法3
# for bai in range(1,10):
#     for shi in range(0,10):
#         for ge in range(0,10):
#             i = bai * 100 + shi * 10 + ge 
#             if x == bai ** 3 + shi**3 + ge**3:
#                 print(i)
            


#自找习题

#有１２３４四个数字能组长多少个不同的三位数
#三个数相同去掉

# for x in range(1,5):
#     for y in range(1,5):
#         for z in range(1,5):
            
#             if x != y != z:
#                 print(x,y,z)
            
        
#  9 * 9 乘法表

# for x in range(1,10):
#     print()
#     for y in range(1,x + 1):   
#         print(x,"*",y,"=",x*y,end = ' ')



# l = []

# while True:
#     s = int(input("请输入整数"))
#     if s == -1:
#         break   #此处ｂｒｅａｋ跳出到哪
#     l.append(s)
#     a = len(l)

# l.reverse()
# print(l)   
# print(a)        
# print(max(l))
# print(min(l))
# print(sum(l)/len(l))

        
#输入多行文字，存入列表中，每次输入回车后算一行
#任意输入多行，当输入回车（即输入空行时结束）    

#１）按　输往返内容在屏幕上输出内容
#2)打印共输入了多少行
#3)打印输入多少字符

# l = []
# i = 0
# b = []
# while True:
#     s = input("输入字符：")
#     if s == '':
#         break
#     # a = list(s)
#     l.append(s)  l += [s]
#     i += 1
# a = len(l)
# print(l)
# print(i,"行")
# count = 0
# for line in l:
#     count += len(line)
# print(count)


#有字符串“ｈｅｌｌｏ”，请用此字符串生成：
#‘ｈｅｌｌｏ’和‘ｈ－ｅ－ｌ－ｌ－ｏ’

# s = 'hello'
# # l = list(s)
# # l = s.split(' ')
# # print(l)
# l = "-".join(s)
# b = " ".join(s)
# print(l)
# print(b)


#写一个程序，让用户输入很多正整数，
#当输入小于０的数时结束输入
#１）打印这些数中最大的数
#2)打印第二大的一个数
#3)删除最小的一个数
#4)打印剩余余数的和

# l = []
# sum = 0
# while True:
#     s = int(input("请输入数据："))
#     if s < 0:
#         break
#     l.append(s)
#     l.sort()
# print(l)
# print("最大为：",l[-1])
# print("第二大为：",l[-2])

# del l[-1]
# print(l)

# for x in l:
#     sum += x
# print(sum)

# import copy 
# L = [3.1,3.2]
# L1 = [1,2,L]
# L2 = copy.deepcopy(L1)
# L2[2][0] = 3.14
# print(L1)   #结果是什么？
# print(L2)   #结果是什么？


# L1 = [1,2,[3.1,3.2]]
# L2 = L1  #不拷贝，创建一个变了同事绑定原对象
# L3 = L1.copy  #浅拷贝　　等同于Ｌ３　＝　Ｌ１
# import copy
# L4 =　copy.deepcopy(L1)   #深拷贝




#练习：
#用列表推导式生成１－１００内奇数的列表
#结果[1,3,5,....100]

# l = []
# l = [x for x in range(1,100,2)]



# L =[x**2 for x in range(1,10) if x%2 !=1]
# print(L)

#练习：
#１．已知有一个字符串
#  s = '100,200,300,500,800'
#　　将其转化为整数的列表存于Ｌ列表中
# 　　　L = [100,200,300,500,800]

# s = '100,200,300,500,800'
# # L = s.split(sep = ',')
# l = s.split(',')
# L = [int(x) for x in l]
# print(l)


# 2.生成前４０个斐波那契数
# １　１　２　３　５　８　１３　......
# 将这些数保存在列表中，打印这些数


#方法1
# a = 0   #a 代表当前数的前1个
# b = 1    #b 代表当前数的前1个
# L = []
# while len(L) < 40:
#     #此处拿到斐波那契数，放入列表中
#     L.append(b)
#     #算出下次循环需要的数
#     # c = a + b
#     # a = b
#     # b = c
#     a,b = b,a + b   #序列赋值不需要c中间变量
# print(L)

# 方法2
# L = [1,1]
# while len(L) < 40:
#     L.append(L[-1] + L[-2])
#print(L)  
       


# ３．有一些数存于列表中：
# Ｌ= [1,3,2,1,6,4,2,....98,82]
# 将列表中出现的数存入到另一个列表Ｌ２中
# 要求：重复出现多次的数字在Ｌ２列表中只保留一份（去重）


# L= [1,3,2,1,6,4,98,82]
# L2 = []
# for x in L:
#     if x not in L2:
#         L2.append(x)
# print(L2)

   
#写程序，实现一下要求： 将如下数据形成一个字典seasons
#  键      值
#  1       春季有1,2,3月
#  2       夏季有4,5,6月
#  3
#  4
#让用户输入整数，代表一个季度，打印信息

# i = 1
# seasons = {}
# seasons[1] = "春季有1,2,3月"
# seasons[2] = "夏季有4,5,6月"
# seasons[3] = "秋季有7,8,9月"
# seasons[4] = "冬季有10,11,12月"
# while i < 5:
#     print(seasons[i],end = '\n')
#     i += 1
# a = int(input("输入整数："))
# if a in seasons:
#     print(seasons[a])
# else:
#     print("不存在！")


#输入一段字符串，打印出这个字符串中出现过得字符的个数
#  输入： abcdabcaba  打印：a :4次  不要求打印顺序


# s = input("输入字符串")
# d = {}
# for ch in s:
#     if ch not in d:
#         d[ch] = 1   
#     else:
#         d[ch] += 1
# print(d)
 

#字符串L = ['tarena','xiaozhang','tyke']
#用上述列表生成如下字典：
# d = {'tarena':6,'xiaozhang':9,'tyke':4}


# L = ['tarena','xiaozhang','tyke']
# d = {}
# for s in L:
#     d[s] = len(s)
# print(d)


# 1.已知有两个等长的列表 list1 和list2
#以list1中的元素为键，以list2中的元素为值，
#生成相应的字典
#list1 = [1001,1002,1003,1004]   
#list2 = ['Tom','Jerry','Spike','Tyke'] 
#生成字典为：
# {1001:'Tom',1002:'Jerru'} 


# i = 0
# # j = 0
# d = {}
# list1 = [1001,1002,1003,1004] 
# list2 = ['Tom','Jerry','Spike','Tyke']
# for x in list1:
#     i += 1
#     for y in list2:
#         j += 1
#         if i == j:
#             d[x] = y
#         if j == len(list2):
#             j = 0      
# print(d)

# while i < 4:
#     d[list1[i]] = list2[i]
#     i += 1
# print(d)





# manager = {"曹操","刘备","孙权"} 
# techs = {"曹操","孙权","张飞","关羽"}

# s1 = manager & techs
# print(s1)

# s2 = manager - (manager & techs)
# print(s2)

# s3 = techs - (manager & techs)
# print(s3)

# s4 = '张飞' in manager
# print(s4)

# s5 = manager ^ techs 
# print(s5)

# s6 = manager | techs 
# print(s6)




# L = []
# while True:
#     a = int(input("请输入数字："))
#     if a < 0:
#         break
#     L.append(a)
# s = set(L)
# print("和为：",sum(L))
# print(s)
# print("和为：",sum(s))




# def myadd(x,y):
#     print(x + y)

# myadd(100,200)
# myadd("abc","300")




# a = int(input("输入数值："))
# def mysum(x):
    # i = 0
    # sum = 0 
    # while i < x + 1:  #最慢
    #     sum += i
    #     i += 1
    # for x in range(1,a + 1):
    #     sum += x
    # print((a + 1) * a/2)  #最快
    # print(sum)

# mysum(a)


# a = int(input("输入数值："))
# b = int(input("输入数值："))
# def mymax(a,b):
#     if a > b:
#         return(a)
#     return(b)
# v = mymax(a,b)
# print(v)


# l = []
# def input_number():
#     while True:
#         a = int(input("输入数值："))
#         if a < 0:
#             break
#         l.append(a)
#     return l


# L = input_number()
# print(L)
# print(max(L))
# print(min(L))
# print(sum(L))







# 练习:
#    1. 写一个函数 print_odd, 打印从begin开始，
#      到end结束(不包含end)内的全部的奇数
#       def print_odd(begin, end):
#           ....

#      print_odd(1, 10)  # 打印 1 3 5 7 9d
#      ptint_odd(10, 20) # 打印 11 13 15 17 19

# begin = int(input("请输入："))
# end = int(input("请输入："))
# def print_odd(begin,end):
#     for x in range(begin,end + 1):
#         if x % 2 == 1:
#             print(x,end = ' ')

# print_odd(begin,end)
# print()

# l = [1,3,5,7,9]
# for x in l:
#     print(x)
   



#    2. 定义两个函数:
#       sum3(a, b, c) 用于返回三个数的和
#       pow3(x)  用于返回x的三次方
#       用以上函数计算:
#         1. 计算1的立方 + 2的立方 + 3的立方的和
#           即:  1**3 + 2**3 + 3**3的和 
#         2. 计算1 + 2 + 3 的和的立方,
#           即:(1+2+3)**3

# a = int(input("请输入："))
# b = int(input("请输入："))
# c = int(input("请输入："))

# def sum3(a,b,c):
#     return(a + b + c)

# def pow3(x):
#     return(x * x * x)
# sum3(a,b,c)
# v = sum3(a,b,c)
# y = pow3(v)
# print(y)



#   3. 改写之前的学生信息管理程序
#      改为两个函数:
#        1. 写一个函数 input_student() 用于返回
#           学生信息的字典的列表(以前格式一样)
#        2. 写一个函数 output_student(lst)
#          此函数传入一个列表lst,即字典的列表
#          此函数把lst的内容以表格形式打印出来
#       def input_student():
#            ....

#       def output_student(lst):
#            ...

#      L = input_student()  # 获取学生信息的列表
#      output_student(L)  # 把L 以列表的形式打印 





# def minmax(a,b,c):
    
#     if a > b:
#         max1 = a
#     else:
#         max1 = b
#     if max1 > c:
#         max1 = max1
#     else:
#         max1 = c

#     if a < b:
#         min1 = a
#     else:
#         min1 = b
#     if min1 < c:
#         min1 = min1
#     else:
#         min1 = c
#     return(min1,max1)
# a = int(input("输入："))
# b = int(input("输入："))
# c = int(input("输入："))
# t = tuple(minmax(a,b,c))
# print(t)

# print("最小：",t[0],"最大：",t[1])



# def myadd(a,b = 0 , c = 0):
#     return(a + b + c)

# print(myadd(10,20))
# print(myadd(100,200,300))


# def  print_odd(a, b = 0):

# if b == 0:
#     for x in range(1,a,2):
#         print(x,end = ' ')
#     else:
#         print()
# else:
#     if a % 2 == 0:
#         a += 1
#     for x in range(a,b,2):
#         print(x,end = ' ')
#     else:
#         print()
      



# def mysumm(*args):
#     sum = 0
#     for x in args:
#         sum += x
#     return sum

# print(mysumm(1,2,3,4))




# 练习：
# 写一个函数，maymax类似于内键的函数max
#详见：
    # >>>help(max)
    # 仿造max写一mymax函数，功能和max完全相同

# def mymax(a ,b ,*args):
#     print(a,b,args)
#     max = 0
#     if a is None and b is None:
#         args.sort()
#         max = args[-1]
#     print(max)
# mymax([3,4,5,6])




# l = []
# def input_number():
#     while True:
#         number = input("输入数字：")
#         if number == '':
#             break
#         l.append(number)

#     return l

# print(input_number())
# print(input_number())




#判断是否为素数
 
# def isprime(a):
#     for x in range(2,a):
#         if a % x != 0:
#             return True 
#         
#     return False

# num = int(input("请输入数字："))
# print(isprime(num))


#返回从m开始到n结束范围内的素数，列表打印

# def prime_m2n(m,n):
#     i = 0
#     lst = []
#     for x in range(m,n):
#         for y in range(2,x):
#             if x % y == 0:
#                 break
        # else:
#             lst.append(x)    
#     return lst

# m = int(input("请输入数字："))
# n = int(input("请输入数字："))

# print(prime_m2n(m,n))




 # 3. 写一个函数pimes(n) 返回小于n的全部
 #    素数的列表,并打印这些素数
 #    如:
 #      L = primes(10)
 #      print(L)  # [2, 3, 5, 7]
 #    1) 打印100 以内的全部素数
 #    2) 打印200 以内的全部素数的和


# def pimes(n):
#     lst = []
#     for x in range(2,n):
#         for y in range(2,x):
#             if x % y == 0:
#                 break
#             if x % y != 0:
#                 if y == x - 1:
#                     lst.append(x)
#     return lst

# def mysum(lst):
#     return sum(lst)

# n = int(input("输入数字："))
# print(mysum(pimes(n)))




 # 4. 编写函数 fn(n) 此函数返回下列级数的和:
 #      fn(n) = 1/(1*2) + 1/(2*3) + .... 
 #      + 1/(n*(n+1)) 的和

 #    print(fn(100))


# def fn(n):
#     sum1 = 0
#     for x in range(1,n + 1):
#         sum1 += 1/(x * (x + 1))
#     return sum1

# n = int(input("输入数字："))
# print(fn(n))


#7月20日







#   2. 写一个生成器函数，生成斐波那契数列的
#   前n个数
#      1 1 2 3 5 8 13
#       def fibonacci(n):
#           ...
#           yield...
#     1) 输出前20个数:
#       for x in fibonacci(20):
#           print(x)
#     2) 打印前40个数的和:
#        print(sum(fibonacci(40)))

# def fibonacci(n):
#     i = 0
#     a = 1
#     b = 1
#     while i < n:
#         c = a +b
#         a = b
#         b = c
#         i += 1
#         yield c
# for x in fibonacci(20):
#     print(x)

# print(sum(fibonacci(40)))

#方法2  违背了yield 函数用意
def fibonacci(n):
    L = [0,1]
    while len(L) <= n + 1:
        yield L[-1]
        L.append(L[-1] + L[-2])
     
#   3. 写程序打印杨辉三角(只打印6层)
#         1
#        1 1
#       1 2 1
#      1 3　3 1
#     1 4　6 4 1
#    1 5　10 10 5 1


# def nn(n):
#     mul1 = 1
#     for x in range(1,n + 1):
#         mul1 *= x 
#     return mul1

# def ii(i):
#     mul2 = 1
#     for y in range(1,i + 1):
#         mul2 *= y
#     return mul2

# def nii(ni):
#     mul3 = 1
#     for x in range(1,ni + 1):
#         mul3 *= x
#     return mul3

# def main():
#     n = int(input("输入层数："))
#     print('1')
#     for x in range(1,n + 1):
#         lst = []
#         i = 0
#         while i < x + 1:
#             ni = x - i
#             if i == 0:
#                 num = 1
#             else:
#                 if i == n:
#                     num = 1
#                 else:
#                     num = int(nn(x) / ii(i) / nii(ni))
#             i += 1
#             lst.append(num)
#             if len(lst) != 1:
#                 pass
#             else:
#                 ' '.join(lst)
#         print(lst)
# main()


# try:
#     #文件的打开和关闭
#     f = open('./sss.doc','w')
#     print('成功')

#     #此处要进行读写操作
#     # s = f.read()
#     # print(s)
#     # print(len(s))
#     f.write('sddlf')
#     print(f)
#     f.close()  #关闭文件

# except OSError:
#     print("打开失败")






# 练习:
#   自己写一个文件 info.txt ，内部存储一些文字
#   信息如下:
#     小张 20 100
#     小李 18 98
#     小王 19 95
#   写程序将这些数据读取出来，打印在屏幕终端上



# w = open('./info.txt')
# l = w.readline(10)
# print(l)
# print(w)




# 练习:
#   1. 写一个程序，输入很多人的姓名，年龄，
#   家庭住址信息,存入文件
#     'infos.txt' 中
#     文件格式自己定义
#     完成输入后查看文件格式是否是你想要的格式
#     (文本文件操`作)

# def sss():
#     lst = []
#     while True: 
#         name = input('输入名字：')
#         if name == '':
#             break
#         num = input('输入号码：')
#         d = {'n':name,'number':num}
#         lst.append(d)

#     return lst

# sss()
# print(sss())


# def rrr(n,m):
#     try:
#         f = open('infos.txt','w')
#         print(s)

#         f.close()

#     except OSError:
#         print('失败！')


# import sys
# while True:
#     s = sys.stdin.readline()
#     if len(s) < 2:
#         break
#     print('刚才读入',len(s),'个字符')
#     print('内容是：',s)

# print('结束')






# 2. 修改学生信息管理程序,要求加入两个功能:
#   9)  保存信息到文件(si.txt)
#   10) 从文件中读取数据(si.txt)
    




# class car:
#     """docstring for  car"""
#     def __init__(self, c,b,m):
#         self.color = c  #'颜色'
#         self.brand = b  #'品牌'
#         self.model = m  #'型号'
#         print('__init__方法被调用')

#     def run(self,speed):
#         print(self.color,'的',self.brand,
#               self.model,'正在以',speed,'速度行驶')

# a4 = car('红色','奥迪','A4')

# a4.run(222)




# class human:
#     '''#以下列表限制此类的对象只有‘name'和’age'属性'''
#     __slots__ = ['name','age']
#     def __init__(self,name,age):
#         self.name,self.age = name,age

# h1 = human("tarena",15)
# print(h1.age)   #15
# # h1.Age = 18     #要是没有__slots__，不会报错
# # print(h1.age)    #15
        
# print(human.__base__)





# static_method.py

# 学生信息有:
#      姓名，年龄，成绩
#   将这些学生对象存于列表中,可以任意添加
#      和删除学生信息
#      1) 打印学生的个数
#      2) 打印出所有学生的平均成绩
#      3) 打印出所有学生的平均年龄
#     (建议用类变量存储学生的个数)


   
# class Student():
#     # i = 0
#     docs = []
#     def __init__(self,name,age,score):
#         self.name = name
#         self.age = age
#         self.score = score
#         # i += 1


#     # def __del__(self):
#         # i -= 1

#     @classmethod
#     def add_student(cls):
#         # while True:
#         #     n = input('姓名：')
#         #     if not n:
#         #         break
#         #     a = int(input('年龄：'))
#         #     s = int(input('成绩：'))
#         #     stu = Student(n,a,s)
#         #     lst.append(stu)
#         s = Student('洗',20,100)
#         cls.docs.append(s)
#         s = Student('d',20,49)
#         cls.docs.append(s)

#     @classmethod
#     def get_student_count(cls):
#         return len(cls.docs)

#     @classmethod
#     def get_avg_score(cls):
#         total = 0.0
#         for s in cls.docs:
#             total += s.score
#         return total / len(cls.docs)

# Student.add_student() #添加学生
# print('当前有%d个学生' % Student.get_student_count(Student.docs))
# print('当前学得会难过的平均成绩是：',Student.get_avg_score(Student.docs))






# super_init.py

# class Human:
#     def __init__(self, n, a):
#         self.name = n
#         self.age = a
#         print("Human.__init__被调用")
#     def infos(self):
#         print("姓名:", self.name)
#         print("年龄:", self.age)

# class Student(Human):
#     def __init__(self, n, a, s):
#         super().__init__(n, a)  # 显式调用父类的初始化方法
#         self.score = s
#         print("Student.__init__被调用")

#     def infos(self):
#         super().infos()
#         print("成绩:", self.score)

# # h1 = Human('小张', 18)
# # h1.infos()
# s1 = Student("魏老师", 35, 60)
# s1.infos()







# 2. 写一个列表类MyList实现存储整数列表,写类
# 的定义如下:
    # class MyList:
    #     def __init__(self, iterator):
    #         self.data = ...
    # 让此类的对象能用for语句进行迭代访问




# class MyList:
#     def __init__(self,iterator):
#         self.data = [x for x in iterator]

#     def __repr__(self):
#         return '%s' % self.data

#     def __iter__(self):
#         self.__next__()

        
#     def __next__(self):
#         ran = 0
#         if self.data > len(self.data):
#             raise StopIteration
#         value = self.data[ran]
#         ran += 1

# L = MyList(range(5))
# print(L)
# L2 = [x ** 2 for x in L]
# print(L2)  # [0, 1, 4, 9, 16]



# # 此示例示意让自定义的作为可迭代对象能让 for 语句迭代访问
# class MyList:
#     def __init__(self, iterable=()):
#         # self.data = [x for x in iterable]
#         self.data = iterable
#     def __repr__(self):
#         return 'MyList(%s)' % self.data

#     def __iter__(self):
#         '''此方法必须返回一个迭代器对象
#         此方法创建一个迭代器对象并返回
#         '''
#         return MyListIterator(self.data)
# class MyListIterator:
#     '''此类用来创建迭代器,此类型的迭代器可以迭代访问
#     MyList类型的对象'''
#     def __init__(self, lst):
#         self.data = lst
#         self.cur_index = 0  # 初始化迭代器的起始位置

#     def __next__(self):
#         '''此方法用于实现迭代器协议'''
#         if self.cur_index >= len(self.data):
#             # 如果索引越界就发终止迭代通知
#             raise StopIteration
#         value = self.data[self.cur_index]  # 要返回的值
#         self.cur_index += 1
#         return value

# myl = MyList([0, -1, 2, -3])
# print(myl)

# # it = iter(myl)
# # print(next(it))

# for x in myl:  # 迭代访问自定义类型的对象
#     print(x)







# 1. 实现两个自定义的列表相加

# class MyList:
#     def __init__(self,lst):
#         self.data = [x for x in lst]
#         # self.data = list(lst) #同上句
#     def __repr__(self):
#         return 'MyList(%s)' % self.data

#     def __add__(self,rhs):
#         i = 0
#         l = []
#         while i < len(self.data):
#             v = self.data[i] + rhs.data[i]
#             l.append(v)
#             i += 1
#         return MyList(l)

#     def __mul__(self,rhs):
#         v = self.data * rhs
#         return MyList(v)

# L1 = MyList([1, 2, 3])
# L2 = MyList(range(4, 7))
# L3 = L1 + L2
# print(L3)  # MyList([1, 2, 3, 4, 5, 6])
# L4 = L2 + L1
# print(L4)  # MyList([4, 5, 6, 1, 2, 3])
# L5 = L1 * 2
# print(L5)  # MyList([1, 2, 3, 1, 2, 3])



# class OrderSet:
#     def __init__(self,lst):
#         # self.data = [x for x in lst]
#         self.data = set(lst)
#     def __repr__(self):
#         return 'OrderSet(%s)' % self.data

#     # def __and__(self,rhs):
#     #     l = []
#     #     for x in self.data:
#     #         for y in rhs.data:
#     #             if x == y:
#     #                 l.append(x)
#     #     return 'OrderSet(%s)' % l

#     # def __or__(self,rhs):
#     #     l = self.data
#     #     for x in rhs.data:
#     #         if x not in l:
#     #             l.append(x)
#     #     return 'OrderSet(%s)' % l

#     def __xor__(self,rhs):
#         l = []
#         s = self.data ^ rhs.data
#         for x in s:
#             l.append(x)
#         return 'OrderSet(%s)' %l


#     def __ne__(self,rhs):
#         if self.data != rhs.data:
#             return 1
#         return 0

#     def __contains__(self,e):
#         return e in self.data


#     def __eq__(self,rhs):



      
# s1 = OrderSet([1, 2, 3, 4])

# s2 = OrderSet([3, 4, 5])

# # print(s1 & s2)  # OrderSet([3, 4])
# # print(s1 | s2)  # OrderSet([1, 2, 3, 4, 5])
# print(s1 ^ s2)  # OrderSet([1, 2, 5])
# if OrderSet([1, 2, 3]) != OrderSet([3, 4, 5]):
#     print("不相等")
# if s2 == OrderSet(3, 4, 5): 这三个变量怎么处理
#     print('s2 == OrderSet(3, 4, 5) is True')
# if 2 in s1:
#     print("2在 s1中")




# class Human:
#     total_count = 0  # 类变量

#     def __init__(self, name):
#         print(name, '对象被创建')


# print(total_count)  # 0









# import pymysql

# #1.创建与数据库连接的对象

# db = pymysql.connect(host = 'localhost',user='root',
#             password='123456',database='db4',
#             charset = 'utf8')

# #2.利用db方法创建游标对象
# cur = db.cursor()

# #3 利用游标对象的execute()方法执行SQl命令
# cur.execute("insert into sheng values\
#             (16,300000,'台湾省');")

# #4.提交到数据库执行
# db.commit()

# print('ok')
# #5 关闭游标对象
# cur.close()

# #6 断开数据库连接
# db.close()




# import pymysql

# db = pymysql.connect(host = 'localhost',user = 'root',
#                      password = '123456',database = 'db4',
#                      charset = 'utf8')

# cur = db.cursor()

# try:
#     cur.execute("insert into sheng values(69,211111,'我的省');")

#     sql_update = "update sheng set id = 686 where id = 78"
#     cur.execute(sql_update)

#     sql_delete = "delete from sheng where s_name = '海南省'"
#     cur.execute(sql_delete)

#     db.commit()
#     print('ok')
# except Exception as e:
#     db.rollback()
#     print('出现错误',e)


# cur.close()

# db.close()        





import pymysql

db = pymysql.connect(host = 'localhost',user = 'root',
                     password = '123456',database = 'db4',
                     charset = 'utf8')

cur = db.cursor()

try:
    sql_select = "select * from sheng;"
    cur.execute(sql_select)

    data1 = cur.fetchone()
    print(data1)
    print("*****************")

    data2 = cur.fetchmany(3)
    # for x in data2:
        # s = x
    print(data2)
    print("*****************")

    data3 = cur.fetchall()
    for x in data3:
        # s = x
        print(x)
    print("*****************")

    db.commit()

except Exception as e:
    print(e)



cur.close()

db.close()   







# -*- coding: cp936 -*-

#??????????

# from random import *

# #?????ͣ?????0???0???10??m???С???s??????????????10??/???J??*???Q??-???K??1???A??.???С???+???????????ķ???????????????????
# cardType=1

# #??ˣ?һ??54????б??ÿ???һ????????
# Deck=[]
# for x in range(2,10):
#     for y in range(0,4):
#         Deck.append(str(x))
# if cardType==0:
#     for x in range(0,4):
#         Deck.append('0')
#         Deck.append('j')
#         Deck.append('q')
#         Deck.append('k')
#         Deck.append('a')
#     Deck.append('s')
#     Deck.append('m')
# else:
#     for x in range(0,4):
#         Deck.append('0')
#         Deck.append('/')
#         Deck.append('*')
#         Deck.append('-')
#         Deck.append('1')
#     Deck.append('+')
#     Deck.append('.')

# #????Ϸ???ƣ???????ݡ????ݿ?????ӷ???ɺ?Ƶ??̬
# Player_Cards=[[],[],[]]
# Player_Cards_backup=[[],[],[]]

# #???
# Bottom_Cards=[]

# #?????Ķ????ע??Ԫ???б?????PASS???????б????б?
# Discard_stack=[]

# #????Ϸ??Ľзַ????-1????δ?з?
# Player_jiaofen=[-1,-1,-1]

# #??ǰ?????????????-1???û???ǰ?Ϸ?
# currentPlayer=-1

# #??ǰ?Ϸ???״̬??ֻ?????ȡֵ??"jiaofen"????з??̬??"playing"????Ϸ?״̬
# state="jiaofen"

# #?????ҵı???-1?????û????
# dizhu=-1

# #?Ϸ?׷?
# difen=0

# #????Ƶ???ַ?x??????ƵĴ??˳????????????1?????Ʋ????
# def card_pow(x):
#     result=-1
#     if x=='3':result=0
#     if x=='4':result=1
#     if x=='5':result=2
#     if x=='6':result=3
#     if x=='7':result=4
#     if x=='8':result=5
#     if x=='9':result=6
#     if x=='0':result=7
#     if x=='j' or x=='/':result=8
#     if x=='q' or x=='*':result=9
#     if x=='k' or x=='-':result=10
#     if x=='a' or x=='1':result=11
#     if x=='2':result=12
#     if x=='m' or x=='.':result=13
#     if x=='s' or x=='+':result=14
#     return result

# #?ѿ??????ard_list???????
# def sort_card(card_list):
#     for i in range(len(card_list)):
#         for j in range(i,len(card_list)):
#             if card_pow(card_list[j])>card_pow(card_list[i]):
#                 card_list[i],card_list[j]=card_list[j],card_list[i]
    
# #?????????????????????Ϊ???????
# def is_cards(str1):
#     for x in str1:
#         if not x in Deck:
#             return False
#     return True

# #?ӿ?Ƭ?б?wn??ȥ??Ƭ?б?is???????????????????alse???ɹ?????rue
# def discard_action(own,dis):
#     own1=own[:]
#     for x in dis:
#         if x in own1:own1.remove(x)
#         else:return False
#     own[:]=own1[:]
#     return True

# #????ʾ????????

# from tkinter import *

# #???򴰿?
# root=Tk()

# #?ؼ?(?)1???зֵ?ѡ??ť?
# list_jiaofen=[]
# v_jiaofen=IntVar()
# for x in range(4):
#     radio=Radiobutton(root,text=str(x),variable=v_jiaofen,value=x)
#     radio.grid(row=0,column=x+1)
#     list_jiaofen.append(radio)
    
# #?ؼ?2???з?????ť
# bt_jiaofen=Button(root,text="jiaofen:  ")
# bt_jiaofen.grid(row=0,column=0)

# #?ؼ?3????Ʊ??
# lb_bottom=Label(root,text='bottom: ')
# lb_bottom.grid(row=1,column=0)

# #?ؼ?4,?ʾ??Ƶı??
# v_bottom=StringVar()
# v_bottom.set('***')
# lb_showBottom=Label(root,textvariable=v_bottom)
# lb_showBottom.grid(row=1,column=1)

# #?ؼ?(?)5,?Ϸ??????
# list_player=[]
# for x in range(3):
#     lb_temp=Label(root,text='player'+str(x)+':   ')
#     lb_temp.grid(row=2+x,column=0)
#     list_player.append(lb_temp)

# #?ؼ?(?)6,?ʾ?Ϸ?????Ƶı??
# list_cards=[]
# v_cards=[]
# for x in range(3):
#     v_temp=StringVar()
#     v_temp.set('*'*17+' '*5)
#     v_cards.append(v_temp)
#     lb_temp=Label(root,textvariable=v_temp)
#     lb_temp.grid(row=2+x,column=1)
#     list_cards.append(lb_temp)

# #?ؼ?(?)7,?ʾ?Ϸ?????????Ƶı??
# list_discards=[]
# v_discards=[]
# for x in range(3):
#     v_temp=StringVar()
#     v_temp.set('*'*3+' '*5)
#     v_discards.append(v_temp)
#     lb_temp=Label(root,textvariable=v_temp)
#     lb_temp.grid(row=2+x,column=2)
#     list_discards.append(lb_temp)

# #?ؼ?(?)8,?ʾ??ǰ????Ϸ??ı??
# list_current=[]
# v_current=[]
# for x in range(3):
#     v_temp=StringVar()
#     if x==0:
#         v_temp.set('<-----')
#     v_current.append(v_temp)
#     lb_temp=Label(root,textvariable=v_temp)
#     lb_temp.grid(row=2+x,column=3)
#     list_current.append(lb_temp)

# #?ؼ?9???????ť
# bt_discard=Button(root,text='discard: ')
# bt_discard.grid(row=5,column=0)

# #?ؼ?10,???????
# v_discard_entry=StringVar()
# en_discard=Entry(root,textvariable=v_discard_entry)
# en_discard.grid(row=5,column=1,columnspan=2)

# #?ؼ?11????ư?ť
# bt_undo=Button(root,text='undo')
# bt_undo.grid(row=6,column=0)

# #?ؼ?12???????ְ?ť
# bt_restart=Button(root,text='restart')
# bt_restart.grid(row=6,column=1)

# #?ؼ?13????????ť
# bt_reset=Button(root,text='reset')
# bt_reset.grid(row=6,column=2)

# #?ؼ?14??״̬?????
# v_state=StringVar()
# v_state.set('state:jiaofen')
# lb_state=Label(root,textvariable=v_state)
# lb_state.grid(row=7,column=0)

# #?ؼ?15????????ֿ?ʼ?İ?ť
# bt_startFromInput=Button(root,text="startFromInput")
# bt_startFromInput.grid(row=8,column=0)

# #?ؼ?16??һ?????򣬿????????ֲ???ʼ??Ҳ???ƾֿ?ʼʱ????ʾ?????ֵ?ַ?????㸴?????
# v_input=StringVar()
# v_input.set(' ')
# en_input=Entry(root,textvariable=v_input)
# en_input.grid(row=8,column=1)

# #ˢ??ʾ?ĺ??
# def refresh_display():
#     #?????ʹ?ȫ?ֱ??????ü??lobal???????????????Ҳһ?
#     global v_bottom
#     global Bottom_Cards
#     global v_current
#     global state
#     global currentPlayer
#     global v_state
#     global v_discards
#     global Discard_stack
#     global dizhu
#     global difen

#     #ˢ??ʾ???
#     v_bottom.set(' '.join(Bottom_Cards))

#     #?????ָʾ??ǰ??ң??????һ???????ı??v_current?????ˢ??ʾ????ҳ?Ƶı??v_cards
#     for x in range(3):
#         v_current[x].set('')
#         sort_card(Player_Cards[x])
#         v_cards[x].set(' '.join(Player_Cards[x]))

#     #?ѵ?ǰ??ҵ??ʾ??????Ϊ??ͷ
#     if currentPlayer>-1 and currentPlayer<3:
#         v_current[currentPlayer].set('<----')

#     #?????????ȷ?????ô???????????ң??֪ʶ?????涼????????
#     if dizhu>-1:
#         v_current[dizhu].set(v_current[dizhu].get()+'*'+str(difen))

#     #?????з??̬???ô???̬?????Ϊjiaofen?????ѳ???ʾ??????Ϊ?зֵ??ֵ
#     if state=="jiaofen":
#         v_state.set('state:jiaofen')
#         for x in range(3):
#             v_discards[x].set(str(Player_jiaofen[x]))

#     #?????Ϸ?״̬???ô???̬?????Ϊplaying?????ÿһ??????ʾ????ʾ???ϴεĳ??
#     if state=="playing":
#         v_state.set('state:playing')
#         for x in range(3):
#             y=(currentPlayer-x-1) % 3
#             #?ʾ?????ϴεĳ??????????????????????˵??Ϸ?տ?ʼû???γ?????ʾΪ??
#             if len(Discard_stack)>x:
#                 v_discards[y].set(' '.join(Discard_stack[len(Discard_stack)-1-x]))
#             else:
#                 v_discards[y].set(' ')
#     return

# #???reset?????ȫ????ʼ
# def reset_click(event):
#     global Discard_stack
#     global Player_jiaofen
#     global currentPlayer
#     global Deck
#     global Player_Cards
#     global Bottom_Cards
#     global Player_Cards_backup
#     global state
#     global dizhu
#     global difen
#     global v_input

#     #??ʼ???׷???
#     difen=0
#     dizhu=-1

#     #??ʼ??????????зּ??
#     Discard_stack=[]
#     Player_jiaofen=[-1,-1,-1]

#     #???ѡһ????ʼ?зֵ??
#     currentPlayer=choice(range(3))

#     #ϴ??????????ѷ????????
#     shuffle(Deck)
#     Player_Cards[0]=Deck[0:17]
#     Player_Cards[1]=Deck[17:34]
#     Player_Cards[2]=Deck[34:51]
#     for x in range(3):
#         Player_Cards_backup[x][:]=Player_Cards[x][:]
#     Bottom_Cards=Deck[51:54]
    
#     #????״̬???Ϊ?з??̬
#     state="jiaofen"

#     #ˢ??ʾ
#     refresh_display()

#     #?ʾ?????ֵ?ַ???
#     v_input.set(''.join(Deck))
    
#     return

# #???restart?????ص??ոշ???Ƶ??̬??Ҳ??ǲ???ϴ????¿???ˣ??????á?
# def restart_click(event):
#     global Discard_stack
#     global Player_jiaofen
#     global currentPlayer
#     global Deck
#     global Player_Cards
#     global Bottom_Cards
#     global Player_Cards_backup
#     global state
#     global dizhu
#     global difen
#     global v_input

#     #??ʼ???׷???
#     difen=0
#     dizhu=-1

#     #??ʼ??????????зּ??
#     Discard_stack=[]
#     Player_jiaofen=[-1,-1,-1]

#     #???ѡһ????ʼ?зֵ??
#     currentPlayer=choice(range(3))

#     #????ϵ?Ʊ?????ı??ݼ??
#     for x in range(3):
#         Player_Cards[x][:]=Player_Cards_backup[x][:]

#     #??????Ϸ״̬Ϊ?з?
#     state="jiaofen"

#     #ˢ??ʾ
#     refresh_display()

#     #?ʾ?????ֵ?ַ???
#     v_input.set(''.join(Deck))
    
#     return

# #???discard???????
# def discard_click(event):
#     global Discard_stack
#     global Player_jiaofen
#     global currentPlayer
#     global Deck
#     global Player_Cards
#     global Bottom_Cards
#     global Player_Cards_backup
#     global state
#     global v_discard_entry

#     #????Ϸ????̬?Ļ????ð????Ч
#     if state!="playing":return

#     #?ӳ??????ȡ??
#     str1=v_discard_entry.get()

#     #???????ַ???????һ????????ϣ???Ч
#     if is_cards(str1)==False:return

#     #??????????Ƴ?????ô?Ͳ???????ˣ??Ϊ?Ϸ??????
#     for x in range(3):
#         if len(Player_Cards[x])==0:return

#     #??????ͨ????˵???Գ???ˡ??ô??????ַ?????һ??????б?????????
#     card_list1=list(str1)
#     sort_card(card_list1)

#     #?????ǰ??ҵ?Ʋ?????????ƣ?Ҳ??Ч??
#     if discard_action(Player_Cards[currentPlayer],card_list1)==False:return

#     #????󣬷???´??룬???????
#     v_discard_entry.set("")

#     #??ӳ?????
#     Discard_stack.append(card_list1)

#     #?ı䵱ǰ??ң?????һ????ҳ??
#     currentPlayer += 1
#     currentPlayer %= 3

#     #ˢ??ʾ
#     refresh_display()
    
#     return

# #???jiaofen?????з֡??????˳????ø????㣬???????Խз֣???????????Ѿ??зֵ?˽еøߣ??ᵱ?ɽз??0??ȫ???з??0?Ļ???Ҳ???Կ?ʼ?Ϸ?ģ??ʱ????????????Ϸ??
# def jiaofen_click(e):
#     global state
#     global currentPlayer
#     global Bottom_Cards
#     global v_jiaofen
#     global Player_jiaofen
#     global dizhu
#     global difen

#     #?ǽз??̬???Ч
#     if state!="jiaofen":
#         return

#     #????зֲ?????ָߣ???????֡????¼?з֡?
#     if v_jiaofen.get()<=max(Player_jiaofen):
#         Player_jiaofen[currentPlayer]=0
#     else:
#         Player_jiaofen[currentPlayer]=v_jiaofen.get()

#     #???ȫ??????з??????ʼ?Ϸ???з??????????ע?ȫ????Ҳ?Ὺʼ?Ϸ
#     if min(Player_jiaofen)>-1:

#         #ȷ???з????????????Ϊ??ǰ??ң?????????
#         max_jiaofen=0
#         for x in range(3):
#             if Player_jiaofen[x]>Player_jiaofen[max_jiaofen]:
#                 max_jiaofen=x
#         currentPlayer=max_jiaofen

#         #????Ϸ״̬Ϊplaying
#         state="playing"

#         #???????ƣ??????????????
#         Player_Cards[currentPlayer]+=Bottom_Cards
#         dizhu=currentPlayer
#         difen=max(Player_jiaofen)

#     #??û??з?????͵??һ????ҽз?
#     else:
#         currentPlayer += 1
#         currentPlayer %= 3

#     #ˢ??ʾ
#     refresh_display()
    
#     return
    

# #???undo?????????γ??
# def undo_click(event):
#     global Discard_stack
#     global Player_jiaofen
#     global currentPlayer
#     global Deck
#     global Player_Cards
#     global Bottom_Cards
#     global Player_Cards_backup
#     global state

#     #????Ϸ????̬???Ч
#     if state!="playing":return

#     #??????û?????????????????Ҳ?Ч
#     if len(Discard_stack)==0:return

#     #??ǰ????????????ѵ?ǰ???趨Ϊ?ոճ?????
#     currentPlayer -= 1
#     currentPlayer %= 3

#     #??Ѿ??????˻?????ǰ??ң?????????????????һ?
#     Player_Cards[currentPlayer]+=Discard_stack.pop()

#     #ˢ??ʾ
#     refresh_display()

#     return

# #???startFromInput??????????ֿ?ʼ?????Ҫ???????????
# def startFromInput_click(event):
#     global Discard_stack
#     global Player_jiaofen
#     global currentPlayer
#     global Deck
#     global Player_Cards
#     global Bottom_Cards
#     global Player_Cards_backup
#     global state
#     global dizhu
#     global difen
#     global v_input

#     #???????ַ??????????ϣ??Ч
#     if is_cards(v_input.get())==False:return

#     #????ַ??????Ϊһ?????˿?
#     deck_list=list(v_input.get())
    
#     #???????ַ????Ȳ??54??Ҳ?Ч??
#     if len(deck_list)!=54:return

#     #??ÿ?????????????????????
#     for x in Deck:
#         if card_pow(x)<13 and deck_list.count(x)!=4:return
#         if card_pow(x)>12 and deck_list.count(x)!=1:return
        
#     #????ϣ??Ч???ʼ?Ϸ
    
#     #??ʼ???׷???
#     difen=0
#     dizhu=-1

#     #??ʼ??????????зּ??
#     Discard_stack=[]
#     Player_jiaofen=[-1,-1,-1]

#     #???ѡһ????ʼ?зֵ??
#     currentPlayer=choice(range(3))

#     #???????ƾַ?????????ݳ?ʼ???
#     Player_Cards[0]=deck_list[0:17]
#     Player_Cards[1]=deck_list[17:34]
#     Player_Cards[2]=deck_list[34:51]
#     for x in range(3):
#         Player_Cards_backup[x][:]=Player_Cards[x][:]
#     Bottom_Cards=deck_list[51:54]

#     #??????Ϸ״̬Ϊ?з?
#     state="jiaofen"

#     #ˢ??ʾ
#     refresh_display()

#     #?ʾ?????ֵ?ַ???
#     v_input.set(''.join(Deck))
    
#     return

# #?󶨸?????ť?????
# bt_jiaofen.bind("<Button-1>",jiaofen_click)
# bt_discard.bind("<Button-1>",discard_click)
# bt_undo.bind("<Button-1>",undo_click)
# bt_reset.bind("<Button-1>",reset_click)
# bt_restart.bind("<Button-1>",restart_click)
# bt_startFromInput.bind("<Button-1>",startFromInput_click)

# #?????֡?????????????????ݵ?¼??????أ???????????ˡ?
# reset_click(0)

# #??????ڱ?Ⲣ??????
# root.title("doudizhu moniqi")
# root.mainloop()







# from pymysql import *

# class Mysqlpython(object):
#     def __init__(self,database,
#                 host="localhost",
#                 user="root",
#                 password="123456",
#                 port=3306,
#                 charset="utf8"):
#         self.host = host 
#         self.user =user 
#         self.password = password
#         self.port = port
#         self.charset = charset
#         self.database = database

#     def open(self):
#         self.db = connect(host=self.host,
#                           user=self.user,
#                           port=self.port,
#                           database=self.database,
#                           password=self.password,
#                           charset=self.charset)
#         sefl.cur = self.db.cursor()

#     def close(self):
  
#         self.cur.close()
#         self.db.close()

#     def zhixing(self,sql,L=[]):    # pymysql.execute(sql)
#         try:
#             self.open()
#             self.cur.execute(sql,L)
#             self.db.commit()
#             print("ok")
#         except Exception as e:
#             self.db.rollback()
#             print("Failed",e)
#         self.close()

#     def all(self,sql,L=[]):
#         try:
#             self.open()
#             self.cur.execute(sql,L)
#             result = self.cur.fetchall()
#             return result
#         except Exception as e:
#             print("Failed",e)
#         self.close()





















