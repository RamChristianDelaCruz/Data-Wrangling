import pandas as pd
#dictionaries
bare1 = {'Student':['Ice Bear','Panda','Grizzly'],
        'Math':[80,95,79]}
bare2 = {'Student':['Ice Bear','Panda','Grizzly'],
        'Electronics':[85,81,83]}
bare3 = {'Student':['Ice Bear','Panda','Grizzly'],
        'GEAS':[90,79,93]}
bare4 = {'Student':['Ice Bear','Panda','Grizzly'],
        'ESAT':[93,89,88]}
#data frame
bears1 = pd.DataFrame(bare1,columns = ['Student','Math'])
bears2 = pd.DataFrame(bare2,columns = ['Student','Electronics'])
bears3 = pd.DataFrame(bare3,columns = ['Student','GEAS'])
bears4 = pd.DataFrame(bare4,columns = ['Student','ESAT'])
#data wrangling
WeBareBears1 = pd.merge(bears1,bears2,
                       on='Student') 
WeBareBears2 = pd.merge(WeBareBears1,bears3,
                       on='Student') 
WeBareBears3 = pd.merge(WeBareBears2,bears4,
                       on='Student') 
#long fomat
Long1=pd.melt(WeBareBears3,id_vars=['Student'],
              value_vars=['Math','Electronics','GEAS','ESAT'],var_name='Subject'
              ,value_name='Grade')
Long2=Long1.sort_values('Student')
Long3=Long2.reset_index()
Final_DataFrame=Long3.drop(columns='index')