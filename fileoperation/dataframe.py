import pandas as pd
df = pd.read_csv(r"C:\Users\tarun\python-demo\fileoperation\customers-100.csv")
print(df.to_string())       # print(df) only starting 5 rows/5 last rows
