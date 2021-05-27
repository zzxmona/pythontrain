def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:", res)


g = foo()
print('--------')
print(next(g))
print("*" * 20)
print(next(g))
print('-----' * 5)
print(next(g), '\n')


# 执行带有yield的函数时，对函数实例化时并不会执行函数
def foo2():
    print("starting...")
    while True:
        res = yield 'z'
        print("res:", res)


g = foo2()
print(next(g))
print("*" * 20)
print(g.send('zzx'), '\n')


def test():
    print('test')
    while True:
        a = yield 'xxx'
        print('a:', a)



t = test()
# print(next(t))
# print(t.send('aaa'))
next(t)
next(t)
t.send('aaa')