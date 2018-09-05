#生成式
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = []
def wyj(L):
    if len(L) == 0:
        print('None')
    else:
        for l in L:
            if isinstance(l,str):
                L2.append(l)
        return L2

# 测试:
print('L2 = ', wyj(L1))
#把一个list中所有的字母都变成小写
L3 = [x.lower() for x in L2]
print('L3 = ', L3)
if L3 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

#列表生成式可以使用两个变量来生成list
dict = {'Akiho Yoshizawa':31, 'Yui Hanato':29, 'Sora Aoi':35, 'Tsukasa Aoi':25}
L4 = [k + '=' + str(v) for k, v in dict.items()]
print(L4)

