import pandas as pd
a={'a':1.0,'b':2.0,'c':3.0}
b=pd.Series(a)


#
data={'Name':['ashok'],'class':['MSC']}
c=pd.DataFrame(data)




#########################
l=[1,2,"apple"]
b=pd.Series(l)
type(b)


c=pd.Series(b,index=(1,2,3))

#############
dict={'Name':'ashok','age':27,'phone':7795801335}
se=pd.Series(dict)

#when se1=pd.Series(dict,index=(10,11,12)) we get the oupt as 10,11,12 and values as NaN NaN Nan
#coz new values will overwrite old values

e=pd.Series(30,index=(0,1,2,3,4,5))

#it will assign 30 for all the indexes



#swapping through index
#when we do this values gets swapped based on the index
dict1={'Name':'ashok','phone':7795801335,'city':'bangalore'}
dict2=pd.Series(dict1,index=['phone','city','Name'])

#extract using index name
dict2['city']


#dataframe
#cloumns->column names

data2=(['Ajay',10],['Akash',11],['Abhi',30]) #tuple cannot convert into dataframe

data1=[['Ajay',10],['Akash',11],['Abhi',30]]#list
d1=pd.DataFrame(data1) #to get the data frame
df=pd.DataFrame(data1,columns=['Name','Age'])#to change column names


#to add one more row
L1=[['ashok',27]]
dadd1=df.append(L1)
###########################    
####Name   Age      0     1
####0   Ajay  10.0    NaN   NaN
####1  Akash  11.0    NaN   NaN
####2   Abhi  30.0    NaN   NaN
####0    NaN   NaN  ashok  27.0

######################################################################
DataFrame1=pd.DataFrame(['Ashok',27])
newData=df.append(DataFrame1)

DataF1=pd.DataFrame(L1)
newdata1=df.append(DataF1)


dictnew1={'Name':'Arun','age':30}
newFrame=pd.DataFrame(dictnew1,index=('Name','Age'))
newdata1=df.append(DataF1)
####################################################

##adding data frames 
newFrame4=pd.DataFrame([['sdbjsfe',387]],columns=['Name','age'])
newFrame3=pd.DataFrame([['ramne',34]],columns=['Name','age'])
newFrame5=newFrame3.append(newFrame4)
newFrame5
 
##       Name  age
##0    ramne   34
##0  sdbjsfe  387

L2=[['sajd',65]]
newFrame7=pd.DataFrame(L2,columns=['Name','age'])
newFrame6=newFrame5.append(newFrame7)


dict4={'Name':['karthik'],'age':[31]}
newFrame8=pd.DataFrame(dict4,columns=['Name','age'])
newFrame9=newFrame6.append(newFrame8)

dict10={'Name':['sdkjf','urreg'],'age':[25,30]}
newFrame10=pd.DataFrame(dict10,columns=['Name','age'])
newFrame11=newFrame9.append(newFrame10)


dict12={'Name':['jh','sdkjf','idfuhg'],'age':[25,30,56]}
newFrame12=pd.DataFrame(dict12,columns=['Name','age'])
newFrame13=newFrame9.append(newFrame12)

newFrame81=pd.DataFrame([['aaaaaaa',65]],columns=['Name','age'])
newFrame91=newFrame8.append(newFrame81)












