import pandas as pd
import matplotlib.pyplot as plt

dict_={'a':[11,21,31],'b':[12,22,32]}

df=pd.DataFrame(dict_)
print(type(df))

print("the output of head is: ", df.head())

print("the output of mean is: ", df.mean())

