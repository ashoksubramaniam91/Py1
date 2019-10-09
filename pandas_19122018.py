import pandas as pd
import numpy as np
import os

os.chdir('')

#to know the number of columns
len(data.rows)
#to know number of rows
len(data)
#to know the number of columns and rows
data.count


#diabetes
Data1


#wine data
Data2
len(Data2.columns)
14-columns

len(Data2)
178-rows

#to get column names
Data2.columns


#mean and standard deviation, variance
N=np.array([10,15,20,25,30,35])
np.mean(N)
np.std(N)
np.var(N)


Data2.loc[Data2['Wine']>=2]

Data2.loc[(Data2['Wine']>=3) | (Data2['Alcohol']>13)]

Data2.loc[(Data2['Wine']>=3) & (Data2['Alcohol']>13)]

Data2.loc[Data2['Wine']!=2]

Data2.loc[Data2['Wine']==2]








