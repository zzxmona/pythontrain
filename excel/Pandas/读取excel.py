import pandas
import sys
import os
import openpyxl

root = sys.path[0]
df = pandas.read_excel(r'{}\\test.xlsx'.format(root))
print(df)
# df2 = pandas.read_excel(r'{}\\test.xlsx'.format(root), sheet_name='Sheet2')
# print(df2)
# df = pandas.read_excel(r'{}\\test.xlsx'.format(root),index_col='姓名')
# print(df)
# df3 = pandas.read_excel(r'{}\\test.xlsx'.format(root),usecols=[0,1])
# print(df3)
# df4 = pandas.read_excel(r'{}\\test.xlsx'.format(root),header=0)
# print(df4)
print(df.head(2))
print(df.shape)
print(df.info())
print(df.describe())

df2 = pandas.read_excel(r'{}\\test.xlsx'.format(root), sheet_name=1)
print(df2.info())
print(df2.isnull())
print(df2.dropna())
print(df2.fillna(0))

# drop_duplicates
print(df2)
print(df2.drop_duplicates(subset='a', keep='last'))
