import math

dic = {
    '1': 'a',
    '2': 'b',
    '3': 'c'
}


# def login():
#     name = input()
#     if name in dic:
#         print(dic[name])
#     else:
#         print('ERROR')
#
# login()

# name=input()
# while name in dic:
#     print(dic[name])
#     break


def prime(s):
    if s < 2:
        return False
    else:
        for i in range(2, s):
            if s % i == 0:
                return False
        else:
            return True


ls = [1, 2, 3, 4, 5, 6]
for item in ls[:]:
    if prime(item):
        ls.remove(item)
print(ls)


a = int(input())
if prime(a):
    print('YES!')
else:
    print('ERROR!')

print([a for a in ls if not prime(a)])