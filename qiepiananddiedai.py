
#递归函数
def fact(n):
     if n == 1:
        return 1
     return n * fact(n-1)

print(fact(3))

#切片
list = ['Akiho Yoshizawa', 'Sora Aoi', 'Yui Hatano', 'Tsukasa Aoi']
print(list[-1])
print(list[0:2])
print(list[-2:])
print(list[:-1])

#习题：去掉str的前后空格
str = ' Akiho Yoshizawa '
def trim(s):
    s = s[1:]
    s = s[:-1]
    return s
print(trim(str),'AV')
print(str.strip(),'AV')

#迭代
dict = {'Akiho Yoshizawa':31, 'Yui Hanato':29, 'Sora Aoi':35, 'Tsukasa Aoi':25}

for key in dict:
    print(key)

for val in dict.values():
    print(val)

for key,val in dict.items():
    print(key,':',val)

for i,value in enumerate(list):
    print(i,value)

#课后习题：使用迭代查找一个list中最小和最大值
from collections import Iterable
def findMinAndMax(L):
    #是否可以迭代
    if not isinstance(L,Iterable):
        print('类型错误')
        return L

    #非空操作
    min = max = None
    if len(L) == 0:
        return (min,max)

    #常规操作
    max = min = L[0]
    for l in L:
        if l <= min:
            min = l
        elif l >= max:
            max = l
            return (min,max)


age = [27, 23, 45, 67, 89, 29, 14, 56, 78]
print(findMinAndMax(age))





