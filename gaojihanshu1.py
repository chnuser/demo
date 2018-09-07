#map()函数实现平方操作f(x)=x2
def f(x):
    return x * x
l = [1, 2, 3, 4, 5]
r = map(f, l)
print(list(r))

#将list所有数字转为字符串
r = map(str,l)
print(list(r))

#reduce()函数1...5相加之和的操作
from functools import reduce
def add(x, y):
    return x + y

r = reduce(add,l)
print(r)

#filter()函数用于过滤序列，
def is_old(n):
    return n % 2 == 1 #注意%与/的区别，这里用到的是余数的概念，余数的计算公式：c = a -⌊ a/b⌋ * b

r = filter(is_old, l)
print(list(r))

#空字符串删除掉
def no_empty(n):
    return n and n.strip()

r1 = ['A', '', 'B', None, 'C', '  ']
r = filter(no_empty,r1)
print(list(r))

#
def by_sorce(L):
    return L[1]

S = [('Akiho Yoshizawa', 30), ('Yui Hanato', 28), ('Sora Aoi', 35), ('Tsukasa Aoi',27)]

r = sorted(S, key=by_sorce, reverse=True)
print(list(r))

#我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f1 = lazy_sum(1,2)
f2 = lazy_sum(1,2)

print(f1() == f2())
