import pandas as pd
# to load dataset
url = "https://raw.githubusercontent.com/coderwolf8152/Gym-Performance-vs.-Nutrition-Analysis/main/gym_nutrition_data.csv"
df = pd.read_csv(url)

print(df.head())
print(df)
# to understand data
#to display concise summary of columns
df.info()
# to display top 20 records
print(df.head(20))
#to display last 10 records
print(df.tail(10))
#to display any 10 random records
print(df.sample(10))
#to display shape of data
print("Shape of data : ",df.shape)
#to view entire data
print(df)
#to display dataype of columns
print("Column dataypes:")
print(df.dtypes)
#to fetch duplicate records
duplicate_record = df[df.duplicated()]
print("Duplicate records : ")
print(duplicate_record)
#to drop duplicate record and obtain unique record
df_unique = df.drop_duplicates()
print("Uinque records : ")
print(df_unique)

