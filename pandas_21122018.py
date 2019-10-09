#Data Pre processing
#importing libraries
#3 essentila libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing dataset
#set working directory
#save the file in the folder and click on RUn or press F5, this will set the folder as working directory

Dataset=pd.read_csv('Wine.csv')

#create matrix for independent(X) [country,age,salary] and dependent variables (Y)[purchased]
X=Dataset.iloc[:, :-1].values
#left side of : is rows######right side is columns
#:-1 means extract all the columns except the last one
print(X)
#we just created matrix for independent variable
#now create for dependent variable
Y=Dataset.iloc[:, 13].values
print(Y)

#missing data
#there are 2 missing datas in the data we have, 1 in age and 1 in salary
#take the mean value of all the other data and fill the missing value
#to do this import scikit
from sklearn.preprocessing import Imputer
#imputer will take care of missing datas
#now create an object for Imputer class
imputer = Imputer(missing_values = 'NaN', strategy = 'mean',axis = 0)
#axis=0-> calculate mean along columns, 1 along rows
#press cntrl+i for help after Imputer
#now fir X with imputer
imputer = imputer.fit(X[: ,1:14])
#just give the indexes of the columns, so v are taking column 1 and 2
X[:, 1:14] = imputer.transform(X[:, 1:14])
#transform will replace all the missing values by the mean
#run the above 4 lines and see the missing values is replaced by mean
print(X)


#encoding categorical data
#in the dataset country and purchased are categorical data
# country contains france spain and germany
#purchase contains yes and no
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_country = LabelEncoder()
X[:, 0] = labelencoder_country.fit_transform(X[:, 0])

#print(X)

#now create dummy encoding, coz since france is 2 and spain is 0, we cannot simply say spain is lesser than france,
#so we create dummy encoding (seperate columns for each country)
# for this we use OneHotEncoder class
#from sklearn.preprocessing import LabelEncoder, OneHotEncoder

onehotencoder = OneHotEncoder(categorical_features = [0])#press cntrl+i for parameter description
#0 means column index
X=onehotencoder.fit_transform(X).toarray()

#now run the #from sklearn.preprocessing import LabelEncoder, OneHotEncoder and the above 2 lines alone
#print(X)
#now in variable explorer click on X and see we have 3 columns for spain, france and germany along with age and salary
#cine the first data is france, then the first column is framce

#now do oit for other column also
#for this we use ly labelencoder, sine ML will understand yes and no
labelencoder_purchased = LabelEncoder()
Y = labelencoder_purchased.fit_transform(Y)
#since Y has only 1 column no need to specify the index
#print(Y)




#splitting data into training and test set
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)#press cntrl+i
#0.2 means 20%, mnormally test size will be 20,25,30%
#now run the above 2 lines
#now x(train& test), Y(train & test) is created in variable explorer
#now we will see whether based on train set we are able to predict the test set and check the results


#feature scaling
#since age and salary are not in same scale this will cause probs in ML models, coz it is based on euclidean distance
#when u use the above formula the range is higher, and square difference of salary dominates  other sauares of age
#thats coz age and salary are not on same scale
#hence we transform the values in same scale from -1 to +1

#############################
"""feature scaling
#--------------

#1)standardisation

#         X(stan)=X-mean(X) / standard deviation (X)

#2)Normalisation,

#        X(norm)=X-X(min)  /  max(X) - min(X) """


###################################
#feature scaling code
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
#for test variables we just need to transform no need to fit and transform
X_test = sc_X.transform(X_test)

#do we need to fit and transform dummy variables?
#yes for more accuracy

#run the above 4 lines

#do we need to apply feature scaling for Y?
#no, coz this is a classification prob with categorical, but for regresion we shld apply feature scaling





