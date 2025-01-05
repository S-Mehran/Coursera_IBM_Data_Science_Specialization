import pandas as pd
import asyncio
import aiohttp
import matplotlib.pyplot as plt
import seaborn as sns
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"
filename = "diabetes.csv"

async def download(url, filename):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                with open(filename, "wb") as f:
                    f.write(await response.read())

async def main():
    await download(url, filename)
    df = pd.read_csv(filename)
    print(df.head())  # Print the first few rows of the dataframe to check
    print(df.info())
    print(df.describe())
    missing_data = df.isnull()
    missing_data.head(5)

    for column in missing_data.columns.values.tolist():
        print(column)
        print (missing_data[column].value_counts())
        print("")    

    labels= 'Not Diabetic','Diabetic'
    plt.pie(df['Outcome'].value_counts(),labels=labels,autopct='%0.02f%%')
    plt.legend()
    plt.show()


# Run the main function
asyncio.run(main())


