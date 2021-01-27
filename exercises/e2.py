# Python 随机数生成
import random
random.randint(1,10)

import numpy as np
np.random.randint(1,10,5)


# 特殊元素的长度
a = [1,2,3,None,(),[],]
print(len(a))

# 交换变量
x=2
y=3
x,y = y,x
print('x的值是%s, y的值是%s' % (x,y))


# 判断数字（以下为截取部分）
def is_number(s):
    try:
        float(s)
        return True
    except:
        pass


is_number('467')  #return返回值只能通过print打印才会显示出来，但在交互式模式下不需要print打印

# 判断质数
s=4
a=[]
for i in range(2, s):
    if s%i==0:
        a.append(i)
if len(a)==0:
        print('%s是一个质数' % s)  #这里的对齐方式很有意思，else居然是跟着这行走的
    else:
        print('%s是一个ssss' % s)

if len(a)==0:        #！！！！！！这个是我常用的
        print('%s是一个质数' % s)
else:
    print('%s是一个ssss' % s)

# 斐波那契数列指的是这样一个数列 0, 1, 1, 2, 3, 5, 8, 13,特别指出：第0项是0，第1项是第一个1。从第三项开始，每一项都等于前两项之和
n=9
lst=[0,1,1]
for i in range(3,n+1):
    a=lst[i-1]+lst[i-2]
    lst.append(a)
print(lst)

#字符串大小写
str = "www.runoob.com"
print(str.upper())          # 把所有字符中的小写字母转换成大写字母
print(str.lower())          # 把所有字符中的大写字母转换成小写字母
print(str.capitalize())     # 把第一个字母转化为大写字母，其余小写
print(str.title())          # 把每个单词的第一个字母转化为大写，其余小写

li=['a', 'b', 'mpilgrim', 'z', 'example']
li.extend('treter')
li

d = dict()
d['z'] = 5
d['b'] = 2
d['c'] = 3
d['d'] = 4

for k in d:
    print(k)