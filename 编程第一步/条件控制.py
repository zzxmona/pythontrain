import random

# end用法，在输出末尾添加值
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a + b
print('\n')

x = random.choice(range(100))
y = random.choice(range(200))
if x > y:
    print('x:', x)
elif x == y:
    print('x+y:', x + y)
else:
    print('y:', y)
print('\n')

a = 1
while a < 10:
    print(a, end=',')
    a += 2
print('\n')
# while else
count = 0
while count < 5:
    print(count, " 小于 5")
    count = count + 1
else:
    print(count, " 大于或等于 5", '\n')

site = ['zzx', 'zx', 'z', 'x']
for x in site:
    if x == 'x':
        print(x)
        break
    print('这次是' + x)
print('\n')

# range()函数,左闭右开
for i in range(5):
    print(i, end=' ')
