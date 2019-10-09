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

#############################################################################
Data1
dd=Data1.describe()
dd.columns
#to get description of only one column
dd[['BloodPressure']]

Data1['Age'].max()

max(Data1['Age'])

len(Data1)

out=Data1.groupby(['Outcome']).size()


#to get the max age whose outcome is 1
d2=Data1.loc[Data1['Outcome']==1]

max(d2['Age'])


#loc-location iwse
#iloc-index wise used for rows
#ix

#to display all the coulmns in the console
 pd.set_option('display.max_columns',12)
 #for rows use rows

#display the max age of all the diabetes patients


s = Data1.groupby('Outcome').Age.mean()









