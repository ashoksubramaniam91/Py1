import numpy as np
a=np.array([1,2,3,4,5,6],dtype=complex,order='C',ndmin=2)
a.reshape(3,2)
x=(1,2,3,4)
i=np.asarray(x,dtype=complex)

odd=np.array([1,2,3,4,5,6,7,8,9,10])
for x in odd:
    if (x%2!=0):
        print(x)
        
j=np.array([1,2,3,4,8,9,10])
k=np.array([1,5,7,9,6,2])
L=np.intersect1d(j,k)



m=np.linspace(1,50,25,endpoint=True,retstep=True)
n=np.logspace(1,100,10,endpoint=True,base=10.0)

#slicing
o=np.arange(10)
p=slice(1,6,2) #or p=slice[1:6:2]
print (o[p])


#broadcasting
q=np.array([[1,2,3],[4,5,6],[7,8,9]])
r=np.array([4,5,6])
s=q+r

#transpose
t=np.arange(0,60,5)
t.shape(3,4)
u=t.T
#to copy
v=np.copy(u)
for x in np.nditer(v):
    print(x)
    
w=np.array([[1,2,3],[4,5,6]])
for x in w:
    print(x)
#sine  
a1=np.array([10,20,30,40,50])
sin=np.sin(a1*np.pi/180)
print(sin)
#sine inverse
a2=np.arcsin(sin)
print(a2)

#topritn in degress
np.degrees(a2)
np.mean(a2)

b2=np.matlib.identity(5,dtype=int)
