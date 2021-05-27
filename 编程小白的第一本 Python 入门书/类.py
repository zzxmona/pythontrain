# 类的实例化最好加()以免报错

class z:
    con = [1, 2, 3, 4]
    name = 'zzx'
    __name = 'zzx'


abc = z()
print(abc.con)
print(z.name)


class two:
    def __init__(self, final):
        self.x = final

    def name2(self):
        print('zzx', '22')

    def name3(self):
        return 'zzx'

    def name4(self, name5):
        print(name5)


x = two('xxx')
print(x.x)
x.name2()
x.name4('zzx name5')


class three():
    def __init__(self):
        self.name = 'zzx'

    def age(self):
        return '22'


test3 = three()
print(test3.name)
print(test3.age())


class CocaCola:
    formula = ['caffeine', 'sugar', 'water', 'soda']

    def __init__(self):
        for element in self.formula:
            print('Coke has {}!'.format(element))

    def drink(self):
        print('Energy!')


coke = CocaCola()


class CocaCola2():
    formula = ['caffeine', 'sugar', 'water', 'soda']

    def __init__(self, logo_name):
        self.local_logo = logo_name

    def drink(self):
        print('Energy!')


coke2 = CocaCola2('可口可乐')
print(coke2.local_logo)
print(coke2.formula)


class five():
    name = 'zzx'
    age = '22'
    sex = '男'

    def __init__(self, id):
        self.id = id

    def lie(self):
        print('{} {} {} {}'.format(self.id, self.name, self.age, self.sex))


f = five(201732110226)
f.lie()


class jcfive(five):
    test = 'test'

    def five2(self):
        print(self.test)


jcfive1 = jcfive('zjnu')
jcfive1.lie()
jcfive1.five2()


class te1():
    def tes1(self):
        return 'tes1'


class te2(te1):
    def tes2(self):
        print('tes2')


t2 = te2()
print(t2.tes1())


class TestA:
    attr = 1

    def __init__(self):
        self.name = 'zzx'
        self.attr = 33
    def rename(self):
        name2 = 'zzx'
        return name2

obj_a = TestA()
print(obj_a.attr)
obj_a.attr = 42
obj_a.name = 'zx'
print(obj_a.attr, obj_a.name)
print(obj_a.rename())
