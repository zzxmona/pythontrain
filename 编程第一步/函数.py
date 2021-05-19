def hello():
    print("hello")


def max(a, b):
    if a > b:
        print(a)
    else:
        print(b)


def a():
    return 1


def change(a):
    print(a)
    a += 1
    print(a)


def zzx(name, age):
    print('name', name)
    print('age', age)


def test(a, *b, **c):
    print(a)
    print(b)
    print(c)


# /指定位置参数，*关键词参数
def f(a, *, b):
    return b


# 匿名函数
zzx = lambda name, age: print(name, age)


def fuc(**kwargs):
    print(kwargs)


hello()
max(1, 2)
print(a())
change(1)
zzx(age=22, name='zzx')
zzx('zx', 22)
test(1, 2, 3, 4, name="zzx", age=22)
print(f(1, b=2))
print('zzx', 22)
fuc(name='zzx', age='22')


def add():
    "Python 函数可以有多个返回值"
    return


print(add.__doc__)
num = 20


def outer():
    num = 10

    def inner():
        global num
        print(num)
        num = 100
        print(num)

    inner()
    print(num)


outer()
print(num)
