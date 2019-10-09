import numpy as mp
A=mp.array([[1,2,3,4],[5,6,7,8]],ndmin=2)
print(A)
a1=mp.array(['ashok',27,7795801335])
print(a1)
a2=mp.array([[1,2,3],[4,5,6]])
print(a2)
type(a2)

arr1 = mp.ndarray((10,4),dtype = object)
arr1[0,:] = int(10)
print(arr1)
arr1[1,:] = float(10)
print(arr1)
arr1[2,:]=complex(1)
print(arr1)

# to extract particular element from an array

#only od numbers
odd=mp.array([1,2,3,4,5,6,7,8,9,10])
for x in odd:
    if (x%2!=0):
        print(x)
        
#to take out only coomon elements in both the array
a1=mp.array([1,2,5,7,9])
a2=mp.array([2,4,6,8,5])

mp.intersect1d(a1,a2)


a1=mp.array(['karthik','shok','sads'])
a2=mp.array(['ashok'])

#to reverse array
a4=mp.array([1,2,3,4,8,10])
a4=a2[::-1]

a5=mp.arange(1,15)


#add these two we will get error
a6=mp.array([1,2,3])
a7=mp.array([2,4,6,8])

a8=a6+a7

# to delete a particular element in an array
a9=mp.array([1,2,3,4,5,6])
a10=mp.delete(a9,2)

# to append elements in an array+
a11=mp.append(a10,12)
a11=mp.append(a10,[10,11,12])

#to sort an array
a12=mp.array([1,10,5,9,12,2])
a13=mp.sort(a12)

#to compare whether 2 arrays are equal or not
a14=mp.array_equal(a12,a13)


# to convert into a string
a15=mp.array2string(a12)


# to convert an array into 2d
a15=mp.atleast_2d(a9)

#to convert an array into 3d
a16=mp.atleast_3d(a9)


#to copy an array
a17=mp.copy(a9,order='K') # default
a18=mp.copy(a9,order='C') # row wise
a19=mp.copy(a9,order='F') # row wise

#to split an array into different arrays
a20=mp.array_split(a12,2)
a21=mp.array_split(a12,3)


#to print union of 2 arrays in 1d
a22=mp.union1d(a12,a11)
#to print union of 2 arrays which are 2d/3d
a23=mp.union1d(a9,a17)











      
        
    



