# python 的宗旨简单、优雅
print("python的宗旨简单、优雅")
print("Hello World!")
print("I\'m \"OK\"")
a = 1
b = 2
if a > b:
    print(True)
else:
    print(False)
# list tuple
list = ['Akiho', 'Yurisa', 'Jelly illi', 'Akiho']
list.append('yui')
list.insert(-1, 'hanato_yui')
print(list[0])

tuple = ('Harden', 'green', 'paul')

for x in list:
    print(x)

for x in tuple:
    print(x)

sum = 0
for s in range(2):
    sum = sum + s
    print(sum)

dict = {'James':33, 'Ginobili':41, 'wyj':30}
print(dict['wyj'])

set = set(['nico', 'taylor', 'cherry', 'nico'])
print(set)

#函数
print(max(dict['wyj'], dict['Ginobili'], dict['James']))

str_age = '123'
age = int(str_age)
print('age =', age)
height = 178
print('height =', str(height))



