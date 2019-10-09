import pandas as pd
dict = {"Number": list(range(1,11,1)),
        "Name": ['Ashok', 'Karthik', 'Naveen', 'Vinoth', 'Arun','ram','murali','sreekanth','jiju','sathya'],
        "Age": list(range(21,31,1)),
        "Gender": ['M','M','F','M','F','M','F','M','M','F']
        }

DF1=pd.DataFrame(dict,columns=['Number','Name','Age','Gender'])


#adding new row to the existing DF

DF2=pd.DataFrame([[11,'sujay',62,'M']],columns=['Number','Name','Age','Gender'],index=[11])
DF3=DF1.append(DF2)

dict1={"Marks":list(range(70,92,2))}

Marks1=list(range(70,92,2))

DF4=pd.DataFrame(dict1,columns=["Marks"])
DF5=DF3.append(DF4)
####################
###DF6=DF3+DF4
######DF6=pd.concat((DF3,DF4),axis=1)


#to add new column
DF3['Marks'] = Marks1
DF3

#to extract a row
DF3.iloc[3]
#df["Name"]
#df(3:4)

#data=pd.read_csv(diabetes.csv)
#pd.read_csv()
#pd.DataFrame()

#to chage the working dicrector
import os
os.chdir('')
getcwd()
#to import csv file
data=pd.read_csv('diabetes.csv')
data.columns
data.head()
data.describe()

#to extract 1 column 
data1=data[["Age"]]


#to extract some rows 
data.iloc[3:10]

data.iloc[3]



