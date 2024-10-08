import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the DataFrame from an Excel file with error handling
try:
    df = pd.read_excel("vissco.xlsx")
except Exception as e:
    print(f"Error loading the Excel file: {e}")
    exit()

# Data info
value = df.info()

# Missing data counts
missing_value = df.isnull().sum()

# Describe the data (categorical)
mean = df.describe(include='object')

# Duplicated data
duplicates = df[df.duplicated()]

# Output
print("Missing Values:\n", missing_value)
print("\nSummary of Categorical Data:\n", mean)
print("\nDuplicated Rows:\n", duplicates)

# Delete duplicates
df.drop_duplicates(inplace=True)
# Show unique and duplicated data
data = df['MRP'].value_counts()
print("\nValue Counts for MRP:\n", data)

# Unique values
unique = df['MRP'].unique()
print("\nUnique Values in MRP:\n", unique)

# Drop rows with NaN in 'MRP'
df.dropna(subset=['MRP'], inplace=True)

# Count of NaN values
count = df['MRP'].isnull().sum()
print("\nCount of NaN Values in MRP:", count)

# Value counts after NaN removal
value_counts = df['MRP'].value_counts()
print("\nValue Counts After NaN Removal:\n", value_counts)

# Print the data type of the 'MRP' column before conversion
print("\nData Type of MRP Before Conversion:", df['MRP'].dtype)

# Convert 'MRP' column to numeric, coercing errors to NaN
df['MRP'] = pd.to_numeric(df['MRP'], errors='coerce')

# Drop any NaN values resulting from the conversion
df.dropna(subset=['MRP'], inplace=True)

# Convert to integers
df['MRP'] = df['MRP'].astype(int)

# Print the data type of the 'MRP' column after conversion
print("\nData Type of MRP After Conversion:", df['MRP'].dtype)

# Check if DataFrame is not empty before saving
if not df.empty:
    # Save the cleaned DataFrame to a new Excel file
    output_file = 'vissco_cleaned_data.xlsx'  # Specify the output file name
    df.to_excel(output_file, index=False, sheet_name='Cleaned Data')  # You can specify a sheet name

    print(f"Data successfully saved to {output_file}")
else:
    print("DataFrame is empty. No data to save.")
