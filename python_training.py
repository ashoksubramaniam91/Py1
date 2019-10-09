x=5
y='ashok'
a=b=c=1
d,e,f=a,'ashok',3
#data types
#numbers
#string
#list
#tuple
#dictionary

#numbers
#int
#float
#long
#complex

#int
g=10
h=-111

#float
l=1.023
m=-4.154
o=4.0e55

#complex
k=2+3j
n=-1j

#strings
str='hello world'
str
str[2]
str[0:5]
str * 2
str + 'ashok'

str.strip()
len(str)
str.lower()
str.upper()

#list
L=[1,2,'ashok',2.23,2j]
L[2]
L[0:3]
for x in L:
    print(x)
    if x==-2:
        break
    elif x==2:
        continue
    
len(L)
L.append(5j)
L.insert(1,20)
L.remove(20)
L.pop()
L.pop(L[1])
L.reverse()
L.sort()
P=L.copy()

#dictionay
d={'name':'ashok','age':27}
d.values()
d.keys()
d['city']='bangalore'
d['city']='chennai','mysore'
    
if 2.23 in L:
    print("element exists")
else:
    print("does not exists")
    
x=10
y=10
if x < y:
    print("x is lesser")
elif x > y:
    print("x is greater")
else:
    print("x is equal to y")


z=0
while z<4:
    print(z)
    z=z+1
################numpy###############
import numpy as np
a=np.array([1,2,3,4])
a[3] 
a=np.array([[1,2,3],[4,5,6]],dtype=float,ndmin=2)


b=np.dtype([('name','s20')],[('age','int1')],[('phone','int4')])    

ar=np.arange(1,25)
ae=np.empty([6,4],dtype=float)
ao=np.ones([5,4],dtype=float)
az=np.zeros([2,3],dtype=complex)


X=(1,2,5,6)
A=np.asarray(X)

Li=[1,2,'ashok']
B=np.asarray(Li)


#odd numbers
Ad=np.arange(10)
Ad
for x in Ad:
    if (x%2!=0):
        print(x)
        
#print common from two arrays
A1=np.array([1,3,5,7,9,8])
A2=np.array([1,5,4,6,9])
np.intersect1d(A1,A2)


#to reverse an array
A3=A1[::-1]
A4=A3.sort


a12=np.array([1,10,5,9,12,2])
a13=np.sort(a12)


##apply packages #deploy
    

