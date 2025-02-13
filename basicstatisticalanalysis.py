import pandas as pd

# Step 2 - Load dataset from a CSV file
df = pd.read_csv("https://raw.githubusercontent.com/coderwolf8152/Gym-Performance-vs.-Nutrition-Analysis/main/gym_nutrition_data.csv")

# Drop duplicate records and obtain unique records
df_unique = df.drop_duplicates()

print("Unique records:")
print(df_unique)
# Basic statistical analysis for numeric columns
print("\nBasic Statistical Analysis:")
print(df_unique.describe())
# Basic statistical analysis for categorical columns
print("\nCategorical Column Analysis:")
print(df_unique.describe(include=['object']))
# Finding missing values
print("\nMissing Values:")
print(df_unique.isnull().sum())