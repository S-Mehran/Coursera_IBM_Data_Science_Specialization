import plotly.express as px
import pandas as pd

# Sales data
data = {
    'Category': ['Electronics', 'Electronics', 'Electronics', 
                 'Furniture', 'Furniture', 'Furniture', 
                 'Clothing', 'Clothing', 'Clothing'],
    'Subcategory': ['Laptops', 'Smartphones', 'Tablets', 
                    'Chairs', 'Tables', 'Sofas', 
                    'Men', 'Women', 'Kids'],
    'Sales': [120000, 80000, 30000, 
              50000, 40000, 20000, 
              70000, 90000, 40000]
}

df = pd.DataFrame(data)

# Creating the treemap
fig = px.treemap(
    df,
    path=['Category', 'Subcategory'],
    values='Sales',
    title='Sales Data Treemap'
)

fig.show()
