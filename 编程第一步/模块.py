import sys
import test
from test import *

print('命令行参数如下:')
for i in sys.argv:
    print(i)
test.fuc1('zzx')
test.fib(1000)
fuc1('zzx')
fib(1000)
print(dir(test))
del test.fib
print(dir(test))
fib(1000)

# os模块
