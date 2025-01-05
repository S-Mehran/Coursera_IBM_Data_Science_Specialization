#import library
import pandas as pd
import numpy as np
import json

#creating a dataframe
df=pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
print(df)

#applying the transform function
df = df.transform(func = lambda x : x + 10)
print(df)

result = df.transform(func = ['sqrt'])
print(result)


person = {
    'first_name' : 'Mark',
    'last_name' : 'abc',
    'age' : 27,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}

