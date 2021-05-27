# 列表
def print1(a):
    return a


listex = [
    1,  # 整数
    1.0,  # 浮点数
    'a word',  # 字符串
    print1('zzx'),  # 函数
    True,  # 布尔值
    [1, 2],  # 嵌套列表
    (1, 2),  # 嵌套元组
    {'key': 'value'}  # 嵌套字典
]
print(listex)

lista = [1]
lista.insert(0, 'zzx')  # insert指定位置新增数据
lista.append('zx')  # append在列表最后新增一个
lista.extend(['x', 'z'])  # extend在列表最后新增列表
print(lista)
# list[a：b]选择list中a-b(不包含b)的数据 语法和字符串一样，所有选择左闭右开，若a=b则未选择
lista[0:0] = ['nb']  # 将第0-0位置上的数据替换0：0指在第一位新增，因为没有选择,
print(lista)
print(lista[0:1])
# 删除列表关键字
del lista[0:0]  # 删除为空
del lista[0:1]  # 删除下标为0的数据

print(lista)
# 字典

dic = {
    'BIDU': 'Baidu',
    'SINA': 'Sina',
    'YOKU': 'Youku'
}
dic2 = listex[-1]
print(dic['BIDU'])
print(dic2['key'])
dic.update({'name': 'zzx', 'age': '22'})  # 通过update向字典中新增键值对
del dic['YOKU']  # 删除元素
print(dic)

# 元组与列表相互转换，元组不可修改数据，元组查看数据方式与列表一致
tuple = tuple(lista)
l = list(tuple)
print(tuple)
print(l)

# 集合
# 集合会删除重复的元素，而且输出没有顺序，可以利用集合判断重属关系
set1 = set('apple')
set2 = set()
print(set)

# 推导式与解析式
# 解析式
b = [i for i in range(10)]
print(b)
print([i for i in b[1:] if i % 2 == 0])

for enumerate, i in enumerate(b): #遍历
    print(enumerate, chr(i+65))
