from pandas import read_csv
from sklearn.feature_selection import VarianceThreshold

df = read_csv(r'D:\Prog\python\CSV dataset\oil-spill.csv',header=None)
data = df.values

print(data.shape)


x = data[:,:-1]
y = data[:,-1]

print(type(x))
print('Values ​​of variable x:\n',x,'\n','Values ​​of variable y:\n',y,'\n')
print(x.shape)

transform = VarianceThreshold(0.1)
x_sel = transform.fit_transform(X=x)

print('Dimensions of variable x:',x_sel.shape)

import numpy as np 

variance = np.arange(0.0,0.55,0.05)
rusalt = []

for t in list(variance):
    transform = VarianceThreshold(t)
    x_sel = transform.fit_transform(X=x)
    n_feature = x_sel.shape[1]
    print(f'Threshold:{t:0.2f} and n_feature:{n_feature}')
    rusalt.append(n_feature)

print(rusalt)
print(x_sel.shape,x.shape)