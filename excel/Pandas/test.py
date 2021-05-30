import pandas

list = ['a', 'b', 'c', 'd']

# Series 一维表
S1 = pandas.Series(list)
print(S1)
print(S1.index)
# 更改索引头
S2 = pandas.Series(list, index=[1, 2, 3, 4])
print(S2)
print(S2.index)

# DataFrame 二维表
df1 = pandas.DataFrame(list)
print(df1)
# 嵌套列表i
df2 = pandas.DataFrame([('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')])
print(df2)
df3 = pandas.DataFrame([('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')], columns=['大写', '小写'])
print(df3)
