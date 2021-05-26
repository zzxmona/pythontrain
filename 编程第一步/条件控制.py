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
print('\n')
for i in range(0, 10, 3):
    print(i, end=' ')
print('\n')

for i in range(len(site)):
    print(i, site[i])
print('\n')
# enumerate 遍历集合、列表、元组；
for i, j in enumerate(site):
    print(i, j)
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('循环结束。', '\n')

for i in range(6):
    for j in range(i):
        print("*", end='')
    print('\r')

print(sum(range(101)))

# pass可以防止语法错误
if a > 1:
    pass

a = [41, 23344, 9353, 5554, 44, 7557, 6434, 500, 2000]
def maopao(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    print(a)
maopao(a)

