import random

counter = 100  # 整型变量
miles = 1000.0  # 浮点型变量
name = "runoob"  # 字符串

print(counter, "  ", type(counter))
print(miles)
print(name)

a = b = c = 1;
print(a, b, c)
a, b, c = 1, 2, 3
print(a, b, c)
print(isinstance(a, int))

# //整除  /除法
print("2/4=", 2 / 4, "\n")
print("2//4=", 2 // 4, "\n")

a = [1, 2, 3, 4, 5, 6]
print(a)
print(a[-1::-1])

a = (1, 2, 3, 4, 5, 6)
print(a[-1::-1])

sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
print(sites)

tinydict = {'name': 'zzx', 'code': 1, 'site': 'fpi'}
print(tinydict.keys())
print(tinydict.values())
print(tinydict)

print(hex(6), "\n")

if 20 == 20:
    print("YES")
else:
    print("NO")

print(random.randrange(0, 100, 2), "\n")

var = "zzx nb"
print(var)
print(var[:3])
print(var[:-3:-1])
print("zzx" in var)
print("zzx\n")
print(r"zzx\n")

print("我叫 %s %s 今年 %d 岁。" % ('zzx', '男', 22))
