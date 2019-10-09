#create random array

import numpy as np
import pandas as pd

df=pd.DataFrame(np.random.randn(5,3),index=['A','B','C','D','E'])

#reindexing or changing the index
df.reindex(index=['E','D','C','B','A'])
#when creating more index we get NAN coz we dont ve any values for that
df1=df.reindex(index=['A','B','C','D','E','F','G','H'])
"""
          0         1         2
A  2.012003  1.026808 -0.233692
B  0.128535 -1.424575  0.860627
C  1.134443 -1.470147  0.368859
D  1.811398 -0.967876 -0.338216
E  0.821609 -0.489302 -0.357079
F       NaN       NaN       NaN
G       NaN       NaN       NaN
H       NaN       NaN       NaN"""
#returns whether the values are null or not like true or false
df1.isnull()
"""       0      1      2
A  False  False  False
B  False  False  False
C  False  False  False
D  False  False  False
E  False  False  False
F   True   True   True
G   True   True   True
H   True   True   True """

#now find mean of each column
np.mean(df[0])

"""to fill na values"""
df2=df1.fillna(np.mean(df1))
"""this fills all the columns mean replacinf na"""
df2=df1.fillna(np.mean(df1[0]))
"""to fill na values for only 1 column"""

"""
          0         1         2
A  2.012003  1.026808 -0.233692
B  0.128535 -1.424575  0.860627
C  1.134443 -1.470147  0.368859
D  1.811398 -0.967876 -0.338216
E  0.821609 -0.489302 -0.357079
F  1.181598 -0.665018  0.060100
G  1.181598 -0.665018  0.060100
H  1.181598 -0.665018  0.060100 """

###############################################################
rdf=pd.DataFrame(np.random.randn(6,4),index=['A','B','C','D','E','F'])
rdf1=df.reindex(index=['A','B','C','D','E','F','G','H','I','J'])
rdf1.isnull()
rdf2=rdf1.fillna(0)
rdf2=rdf1.fillna(np.mean(rdf1[0]))

""" 
          0         1         2
A  2.012003  1.026808 -0.233692
B  0.128535 -1.424575  0.860627
C  1.134443 -1.470147  0.368859
D  1.811398 -0.967876 -0.338216
E  0.821609 -0.489302 -0.357079
F  1.181598  1.181598  1.181598
G  1.181598  1.181598  1.181598
H  1.181598  1.181598  1.181598
I  1.181598  1.181598  1.181598
J  1.181598  1.181598  1.181598"""
rdf2=rdf1.dropna()
""" if the following rows are na, then it will copy the last row values to all the nas"""
rdf2=rdf1.fillna(method='pad')

"""           0         1         2
A  2.012003  1.026808 -0.233692
B  0.128535 -1.424575  0.860627
C  1.134443 -1.470147  0.368859
D  1.811398 -0.967876 -0.338216
E  0.821609 -0.489302 -0.357079
F  0.821609 -0.489302 -0.357079
G  0.821609 -0.489302 -0.357079
H  0.821609 -0.489302 -0.357079
I  0.821609 -0.489302 -0.357079
J  0.821609 -0.489302 -0.357079 """

""" to delete a column"""
del rdf1[2]

"""
          0         1
A  2.012003  1.026808
B  0.128535 -1.424575
C  1.134443 -1.470147
D  1.811398 -0.967876
E  0.821609 -0.489302
F       NaN       NaN
G       NaN       NaN
H       NaN       NaN
I       NaN       NaN
J       NaN       NaN"""



"""to delete a row"""
rdf4=rdf1.drop('G')

"""          0         1
A  2.012003  1.026808
B  0.128535 -1.424575
C  1.134443 -1.470147
D  1.811398 -0.967876
E  0.821609 -0.489302
F       NaN       NaN
H       NaN       NaN
I       NaN       NaN
J       NaN       NaN"""

"""to insert a row, create one more dataframe and append it"""

rdf5=pd.DataFrame(np.random.randn(1,3),index=['K'])
rdf6=rdf4.append(rdf5)


"""to add a column"""
sLength = len(rdf8[0])
rdf8['e'] = pd.Series(np.random.randn(sLength), index=rdf8.index)
"""
          0         1         2         e
A  2.012003  1.026808       NaN -0.793249
B  0.128535 -1.424575       NaN  0.844273
C  1.134443 -1.470147       NaN -0.281648
D  1.811398 -0.967876       NaN  1.621229
E  0.821609 -0.489302       NaN  0.996181
F       NaN       NaN       NaN  0.628325
H       NaN       NaN       NaN  1.611596
I       NaN       NaN       NaN  0.187935
J       NaN       NaN       NaN  0.945515
K  0.567085 -0.586821 -0.890030  1.656995
G -0.320646 -0.055024 -0.080337 -2.406061"""

