import pandas as pd 
std_data=[(1,'megha','sisana'),(2,'rakhi','baghpat')]
df=pd.DataFrame(std_data,columns=['ID','name','address'])
print(df)

#operations on table
print(df['name'])     # print cloumns

print(df.loc[1])      #print row with the specified index

