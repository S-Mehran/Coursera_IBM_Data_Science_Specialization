import pandas as pd
Student_data = {"Student": ["David", "Samuel", "Terry", "Evan"], "Age": [24, 27, 22, 21], "Country": ["UK", "Canada", "China", "USA"], "Course": ['Python', 'Data Structures', 'Machine Learning', 'Web Development'], "Marks": [85, 72, 89,76]}

data_frame =  pd.DataFrame(Student_data)
print(data_frame)

b = data_frame[['Marks']]
print(b)

c = data_frame[['Country', 'Course']]
print(c)


d = data_frame.iloc[0,2]
print(d)
e = data_frame.loc[3, 'Course']
print(e)

f = data_frame.iloc[0:2, 0:3]
print(f)
w = data_frame.iloc[1:3, 2:4]
print(w)

