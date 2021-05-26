# replace 用法
import sys

phone_number = '1386-666-0006'
hiding_number = phone_number.replace(phone_number[:9], '*' * 9)
print(hiding_number)

data = [1, 3, 1, 4, 5, 6, 8, 1, 2, 3]
for i in range(len(data)):
    if data[i] > 5:
        print(i)
        break

print(next(i for i, x in enumerate(data) if x > 5))
data = iter(data)

# while True:
#     try:
#         print(next(data), end=' ')
#     except StopIteration:
#         sys.exit()

search = '168'
num_a = '1386-168-0006'
num_b = '1681-222-0006'
print(search + ' is at ' + str(num_a.find(search) + 1) + ' to ' + str(num_a.find(search) + len(search)) + ' of num_a')
print(search + ' is at ' + str(num_b.find(search) + 1) + ' to ' + str(num_b.find(search) + len(search)) + ' of num_b')

# format替换三种方式
print('{}{}'.format('a', 'b'))
print('{a}{b}'.format(a='a', b='b'))
print(('{0}{1}'.format('a', 'b')))
