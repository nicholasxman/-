# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
s = 0
for a in range(1, 5):
    for b in range(1, 5):
        for c in range(1, 5):
            if a != b and b != c and a != c:
                print(100*a+10*b+c)
                s +=1
print(s)

# 题目：企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10 %；利润高于10万元，低于20万元时，低于10万元的部分按10 % 提成，高于10万元的部分，可提成7.5 %；
# 20万到40万之间时，高于20万元的部分，可提成5 %；
# 40万到60万之间时高于40万元的部分，可提成3 %；
# 60万到100万之间时，高于60万元的部分，可提成1.5 %，高于100万元时，超过100万元的部分按1 % 提成，从键盘输入当月利润I，求应发放奖金总数？
i =110
if i <= 10:
    print(0.1 * i)
elif i<=20:
    print(10*0.1+0.075*(i-10))
elif i <= 40:
    print(10*.1+10*.075+(i-20)*0.05)
elif i <= 60:
    print(10*0.1+10*0.075+20*0.05+(i-20)*0.03)
elif i <=100:
    print(10*0.1+10*0.075+20*0.05+20*0.03+(i-60)*0.015)
else :
    print(10*0.1+10*0.075+20*0.05+20*0.03+40*0.015+(i-100)*0.01)

i=110
rank=[100,60,40,20,10,0]
profit=[0.01,0.015,0.03,0.05,0.075,0.1]
money=0
for a in range(6):
    if i>rank[a]:
        money += (i-rank[a])*profit[a]
        print(money)
        i=rank[a]
        print(i)
print(money)


# 题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

# 题目：输入某年某月某日，判断这一天是这一年的第几天？

# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。

# 题目：将一个列表的数据复制到另一个列表中。
a=[1,2,3,4,5]
b=a[:]
print(b)

# 题目：输出 9*9 乘法口诀表。
i=list(range(1,10))
# j=list(range(1,10))
for raw in i:
    for column in range(1,raw+1):
        print('%s*%s=%s' % (raw, column, raw*column),end='\t')   #end='\t'这玩意的作用！！！
    print('')
    # print('???')

# 题目：暂停一秒输出。
import time
for i in range(5):
    print(i)
    time.sleep(1)

# 题目：暂停一秒输出，并格式化当前时间。
import time
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
time.sleep(1)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

# 题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？

# 题目：判断101-200之间有多少个素数，并输出所有素数。
s=0
list1 = list(range(101, 200))
print(list1)
list2=[]
for i in range(2,100):
    for j in range(2, 100):
        if 100<i*j<200:
            list2.append(i*j)
            print(i * j)
print(list2)
list3=list(set(list2))
list4=sorted(list3,key=list2.index)  #列表的顺序的作用
print(list4)
for num in list1:
    if num not in list4:
        print(num)
        s+=1
print(s)

# 题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
x=range(1,10)
y=range(10)
z=range(10)
for i in x:
    for j in y:
        for k in z:
            if i**3+j**3+k**3==100*i+10*j+k:
                print(i,j,k)

# 题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
n=60
list5=[]
while n>1:
    for i in range(2,int(n)+1): #!!!!!!!!!!!!!如果这里写n 会卡死在这
        if n%i ==0:
            n=int(n)/i
            print(int(n))
            list5.append(i)
            break
print(list5)
print('*'.join(str(i) for i in list5))

# 题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
score=60
lst1=[90,60,0]
lst2=['A', 'B', 'C']
for i in range(3):
    if score>=lst1[i]:
        print(lst2[i])
        break

if score>=90:
    grade='A'
elif score>=60:
    grade='B'
else:
    grade='C'
print('%s属于%s' % (score, grade))

# 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
str2='df即可韩国dsf423 !^*&*(g4,ss'
len(str2)
str2.count('s')
str2.index('f')
str2.isalpha()

# 题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
