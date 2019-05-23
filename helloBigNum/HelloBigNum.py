from pandas import Series
from pandas import DataFrame

ser = Series([1,2,3,4,5])

print(ser)
print(ser.index)
print(ser.values)

otherSer = Series(index=['one', 'two', 'three', 'four', 'five'], data=[1, 2, 3, 4, 5])
print(otherSer)
print(otherSer.index)
print(otherSer.values)

df = DataFrame({
    'name' : ['one', 'two', 'three', 'four', 'five'],
    'age' : [20, 30, 40, 50, 60],
    'sex' : ['nan', 'nv', 'nan', 'nan', 'nan'],
    'money' : [1.1, 1.2, 1.3, 1.4, 1.5]
})
print(df)
print(df * 3)
print(df['age'])
print(df['age'].values)
newdf = DataFrame({
    'age' : df['age'].values,
    'money' : df['money'].values
})
print(newdf)
print(newdf * newdf)