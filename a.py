import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('owid-co2-data.csv')

# Drop duplicate rows based on the "Country" column
df.drop_duplicates(subset=['country'],keep="first", inplace=True)

# Save the cleaned DataFrame to a new CSV file
df.to_csv('owid-co2-data_cleaned.csv', index=False)


# # Read the cleaned CSV file into a DataFrame, specifying the index column
df = pd.read_csv('owid-co2-data_cleaned.csv', index_col=0)

# # Save the index column to a new CSV file
df.index.to_series().to_csv('a.csv', header=False, index=False)