a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a.insert(0, 10)
print(a)
a.reverse()
print(a)
a.remove(10)
print(a.count(1))
del a[:]
a.append("zzx")  # 添加一个值
a.clear()
a.extend(["zzx", "zx", "z", "x"])  # 添加指定列表
print(a)
print(a.pop(), a.pop())
print(a)
print([3 * x for x in a])  # 重复三遍
print([[x, x, 3 * x] for x in a])
print([3 * x for x in a if len(x) > 2])
b = [1, 2]
print([[x, y] for x in b for y in a])
print([x + str(y) for x in a for y in b])

# 嵌套列表
c = [[1, 2, 3, 4], ["zzx", "zx", "z", "zx"], [999, 888, 777, 666]]
print(c)
print([[row[i] for row in c] for i in range(4)])
d = []
for i in range(max([len(row) for row in c])):
    d.append([row[i] for row in c])
print(d)
c = [[1, 2, 3, 4, 5], ["zzx", "zx", "z", "zx"], [999, 888, 777, 666]]
print(max([len(row) for row in c]))
del c[0][0]
print(c)
d = c[1]
print([x for x in d])
print(sorted([x for x in d]))