import pandas as pd
std_data=[(1,'megha','sisana'),(2,'rakhi','baghpat')]
df=pd.DataFrame(std_data,columns=['ID','name','address'])
print(df.head(1))       # top 5 rows if limit not given
print(df.tail(1))       # last 5 rows 
print(df.shape)         # no. of rows and cols.
print(df.columns)       # name of columns
print(df.size)          # total elements
print(df.dtypes)        # dataype
print(df.values)        # all values in list form 
print(df.index)         # value of index,start,stop