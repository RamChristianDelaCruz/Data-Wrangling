import pandas as pd
#dictionary
Dictionary={'Box':['Box1','Box1','Box1','Box2','Box2','Box2'],
   'Dimension':['Length','Width','Height','Width','Length','Height'],
   'Value':[6,4,2,5,3,4]}
#data frame
Messy=pd.DataFrame(Dictionary,columns=['Box','Dimension','Value'])
#data wrangling
Tidy=Messy.pivot_table(index=['Box'],columns='Dimension',values='Value')
Final_DataFrame=Tidy.reset_index()
#New column
Final_DataFrame['Volume']=Final_DataFrame.Length*Final_DataFrame.Width*Final_DataFrame.Height