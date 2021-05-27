album = ['Black Star', 'David Bowie', 25, True]
print(album)
album.append("zzx")
print(album[0], album[-1])
print('zzx' in album)


# 条件控制
def login():
    # username = input("账户：")
    # password = input('密码：')
    username = 'zzx'
    password = '123456'
    if username == 'zzx' and password == '123456':
        print('Login Success!')
    else:
        print('Fail!')
        login()


# Loop 循环
def loop():
    print(album)
    for i in range(len(album)):
        print(album[i], end=' ')
    print('\r')
    for i in album:
        print(i, end=' ')


# 嵌套循环
def forloop():
    for i in range(1, 10):
        for j in range(1, 10):
            print('{}X{}={}'.format(i, j, i * j).rjust(6), end=' ')
        print('\r')


# while循环
def whileloop():
    const = 1
    while 1 == 1:
        print(const, end=' ')
        const += 1
        if const > 5:
            break


login()
loop()
forloop()
whileloop()
