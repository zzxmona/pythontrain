import sys

a = [1, 'a', 2, 'b', 'zzx', 'c']
print('列表部分方法')
print(a)
print(a.count('zzx'))
print(a.index('zzx'))
print(a.pop(-2))
print(a)
a.reverse()
print(a)
print(tuple(a), '\n')

tup = (1, 'a', 2, 'b', 'zzx', 'c')
tup2 = ('www', 'kkk')
print('元组部分方法')
print(tup[0])
print(tup[2:])
print(tup + tup2)
print(len(tup))
print(max(tup2))
print(list(tup))
print(id(tup), '\n')

zzx = {'name': 'zx', 'sex': '男', 'age': '22'}
print('字典部分')
print(zzx['name'], zzx['age'])
zzx['name'] = 'zzx'
print(zzx['name'])
print(str(zzx))
print(len(zzx))
print(zzx.keys())
print(zzx.popitem())
print(zzx.pop('name'))
zzx.update({'name': 'zx', 'age': '22'})
print(zzx, '\n')

a = set('123456')
b = set('345678')
print('集合部分')
print(a - b, a | b, a & b, a ^ b)
a.update({'a', 'b'}, ['zzx', 'zx'], {'name': 'x'})
print(a)
a.discard('zx')
print(a)
