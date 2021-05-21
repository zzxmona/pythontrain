import request

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
    print(repr(x * x * x).rjust(4))
print('\n')
print('姓名：{name},年龄:{age}'.format(age=22, name='zzx'))
a = {'zzx': 1, 'zx': 2, 'z': 3, 'x': 4}
for i, j in a.items():
    print('{0:3} => {1}'.format(i, j))


# a = input("请输入:")
# print(a)


# 文件的读写
def openf():
    str = 'C:\\Users\\26279\\Desktop\\py测试文件.txt'
    o = open(str, 'w')
    o.write("----乘法口诀表----\n")
    for i in range(1, 10):
        for j in range(1, i + 1):
            o.write(repr(i * j).rjust(3))
        o.write('\n')
    o.close()
    r = open(str, 'r+')
    print(r.read())
    line = r.readline()
    print(line,"zzx")
    r.close()


openf()

