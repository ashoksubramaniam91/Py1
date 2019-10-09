import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#for line plot
x=np.array([1,2,3,4,5])
y=np.array([1,2,3,4,5])

plt.plot(x,y)

#give some options like 
plt.plot(x,y,'bo')

plt.plot(x,y,linestyle='dashed')

#used for linear regression

##############################################################
#histogram

Z=np.array([10,20,30,40,50])
plt.hist(Z)

A=np.arange(10,110,5)
plt.hist(A,bins=[0,20,40,60,80])

Data=pd.read_csv('C:\\Users\\Ashok\\Downloads\\diabetes.csv')

Data.columns

plt.hist(Data['Age'])
#to fine max of age who has diabetes
s = Data1.groupby('Outcome').Age.max()

b=Data[Data['Outcome']==1]['Age'].max()

b=Data['Outcome']['Age'].max()
plt.hist(s)

#do labes




