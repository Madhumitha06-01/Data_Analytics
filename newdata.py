import pandas as pd

# Read the Excel file
df = pd.read_excel("vissco.xlsx")

# Count and print duplicates
duplicates = df.duplicated().sum()
print(f"Number of duplicates: {duplicates}")

# Drop duplicates
df.drop_duplicates(inplace=True)

# Fill NaN values for specified columns with 'N/A'
newdata = df.fillna({'ITEMNAME': 'N/A', 'SUMMARY': 'N/A', 'CODE': 'N/A', 'DETAILS': 'N/A', 'SPECIFICATION': 'N/A','IMAGE_URL':'N/A'})

# Apply backward fill only to the 'MRP' column
newdata['MRP'] = df['MRP'].fillna(method='ffill')

# Print the new DataFrame
print(newdata)
print(f"Shape after cleaning: {newdata.shape}")

# Save the cleaned DataFrame to a new Excel file
new_file_name = "cleaned_vissco.xlsx"
with pd.ExcelWriter(new_file_name, engine='openpyxl') as writer:
    # Write the new DataFrame to a new sheet
    newdata.to_excel(writer, sheet_name='CleanedData', index=False)

print(f"Cleaned data saved to {new_file_name}")
