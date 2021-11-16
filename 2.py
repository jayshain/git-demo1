import pandas as pd
df=pd.read_clipboard()
print(df)
df.to_csv('匯率.csv')