import pandas as pd
from numpy import unique

data_oil_spill = pd.read_csv(r'D:\Prog\python\CSV dataset\oil-spill.csv',header=None)
print(data_oil_spill.shape)

data = data_oil_spill.values

# for i in range(data.shape[1]):
#     print(i,len(unique(data[:,i])))
#ndarray
print(f'The first data to the fifth data of the first column :\n{data[0:5,1]}\n')
#dataframe
print(data_oil_spill.nunique())

#Delet columns That Contain a Singel Value

conts = data_oil_spill.nunique()
print(list(enumerate(conts)))

to_del = [i for i,v in enumerate(conts) if v == 1]
# list_coprehension = [expression for item in iterable if statement(condition)]
print('Indexes whose values ​​are repeated only once :',to_del)
data_oil_spill.drop(to_del,axis=1,inplace=True)

for i in range(data.shape[1]):
    num = len(unique(data[:,i]))
    percentage = float(num) / data.shape[0] * 100
    print('%d ,%d, %.1f%%'%(i,num,percentage))

todel = [i for i,v in enumerate(conts) if (float(v)/data.shape[0]*100<1)]

print(todel)






