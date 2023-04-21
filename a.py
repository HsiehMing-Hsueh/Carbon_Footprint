import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('owid-co2-data.csv')

# Drop duplicate rows based on the "Country" column
df.drop_duplicates(subset=['country'], inplace=True)

# Save the cleaned DataFrame to a new CSV file
df.to_csv('owid-co2-data_cleaned.csv', index=False)