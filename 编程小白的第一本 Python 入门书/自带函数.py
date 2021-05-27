print(divmod(7, 2))  # 商和余数，元组格式


class C:
    @staticmethod  # 静态方法不需要实例化
    def f():
        print('runoob')


C.f()  # 静态方法无需实例化

data = ['a', 'b', 'c']
print(list(enumerate(data)))  # 遍历数组,带有下标
print(list(enumerate(data, start=1)))  # 更改遍历下标

for i, enumerate in enumerate(data):  # 输出
    print(i, enumerate)

str1 = str(data)
str2 = eval(str1)
print(type(str2))

print(isinstance('zzx', str))
