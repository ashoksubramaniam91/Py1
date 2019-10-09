##panda
#how to install panda
#open anaconda cmd prompt
#type conda and enter
#type conda install pandas
#in cosole
#import pandas as pd
import numpy as np
import pandas as pd

a=np.array([1,2,3,4,5])
b=pd.Series(a,Series=(1,2,3,4,5))
b=pd.Series(a,Index=(1,2,3,4,5))

data=[1,2,3,4,5]
c=pd.DataFrame(data)




