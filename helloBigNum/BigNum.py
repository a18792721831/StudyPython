from pandas import Series
from pandas import DataFrame

inde = ['x1', 'x2', 'x3', 'x4', 'x5']
oneSer = Series(data=[1, 2, 3, 4, 5], index=inde)
twoSer = Series(data=[2, 4, 6, 8, 10], index=inde)
threeSer = Series(data=[1, 3, 5, 7, 9], index=inde)

x1 = DataFrame([oneSer, twoSer, threeSer])

print(x1)

inde2 = ['y1', 'y2', 'y3']
yoneSer = Series(data=[1, 2, 3], index=inde2)
ytwoSer = Series(data=[4, 5, 6], index=inde2)
ythreeSer = Series(data=[7, 8, 9], index=inde2)
yfourSer = Series(data=[10, 11, 12], index=inde2)
yfiveSer = Series(data=[13, 14, 15], index=inde2)

y1 = DataFrame([yoneSer, ytwoSer, ythreeSer, yfourSer, yfiveSer])

print(y1)

for rx in x1.values:
    print(rx)
    for cy in y1.colums:
        print(y1[cy])
        for i in y1[cy].index:
            print(rx[i] * y1[cy][i])