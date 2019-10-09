rdf9['e'] = p.Series(np.random.randn(sLength), index=rdf8.index)
sLength = len(df1[0])
rdf9['e'] = pd.Series(np.random.randn(sLength), index=rdf8.index)
rdf9['e'] = pd.Series(np.random.randn(sLength), index=rdf8.index)
sLength = len(rdf8[0])
rdf9['e'] = pd.Series(np.random.randn(sLength), index=rdf8.index)
sLength = len(rdf8[0])
rdf8['e'] = pd.Series(np.random.randn(sLength), index=rdf8.index)
rdf8

## ---(Mon Dec 24 12:47:25 2018)---
import matplotlib.pyplot as plt
import numpy as np
line=np.array([1,2,3,4,5],[1,2,3,4,5])
line=np.array([[1,2,3,4,5],[1,2,3,4,5]])

line
x=np.array([1,2,3,4,5])
y=np.array([1,2,3,4,5])


plt.plot(x,y)
plt.plot(x,y,'bo')
plt.plot(x,y,linestyle='dashed')
Z=np.array([10,20,30,40,50])

Z
plt.hist(Z)
Z=np.array([10,20,30,40,50])
y=np.array([1,2,3,4,5])
plt.hist(Z,y)


Z=np.array([10,20,30,40,50])
plt.hist(Z,y)


Z
plt.hist(Z)

A=np.arange(10,110,10)
A
A=np.arange(10,110,10)
plt.hist(A,bins=[0,20,40,60,80])



A
A=np.arange(10,110,10)
plt.hist(A,bins=[0,20,40,60,80,100])


Data=pd.read_csv('C:\\Users\\Ashok\\Downloads\\diabetes.csv')
import pandas as pd
Data=pd.read_csv('C:\\Users\\Ashok\\Downloads\\diabetes.csv')
Data.columns
plt.hist(Data['Age'])
Data[['Outcome']==1]['Age'].mean()
Data
Data[['Outcome']==1]['Age'].mean()
Data1=Data['Outcome']
Data1
Data[['Outcome']==1]['Age'].mean()
Data[['Outcome']==1]['Age']
Data[['Outcome']==1]['Age'].mean()
s = Data1.groupby('Outcome').Age.mean()
s = Data.groupby('Outcome').Age.mean()
s
plt.hist(s)
b=Data.groupby('Age')
b
c=Data.groupby('Age').count()
c
b=Data.groupby('Age').count(Outcome)

b=Data.groupby('Age').count('Outcome')
b=Data.groupby('Age').count()
b
c=Data['Outcome']['Age'].max()

c=Data['Age'].max()
c
d2=Data1.loc[Data1['Outcome']==1]
d2=Data.loc[Data['Outcome']==1]
d2
max([d2])
d.['Age'].max()
d2['Age'].max()
s = Data1.groupby('Outcome'==1).Age.max()
s = Data.groupby('Outcome'==1).Age.max()
s = Data.groupby('Outcome').Age.max()
s
s = Data.groupby(('Outcome')==1).Age.max()
s = Data.groupby(['Outcome']==1).Age.max()
s = Data.groupby('Outcome').Age.max()
s
b=Data['Outcome']['Age'].max()
b=Data[['Outcome']]['Age'].max()
b=Data[['Outcome']['Age']].max()
b=Data[Data['Outcome']==1]['Age'].max()
b

## ---(Wed Dec 26 19:37:12 2018)---
import pandas as pd
import numpy as np
import matlplotlib.pyplot as plt
import matplotlib.pyplot as plt