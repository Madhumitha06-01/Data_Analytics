import pandas as pd

# Read the Excel file
df = pd.read_excel("Master Copy of CITAACC LTMs - 09 Nov 24.xls")

# Clean columns "Name / Batch / Branch" by removing everything after the "/"
for column in ['Name / Batch / Branch']:
    if column in df.columns:
        df[column] = df[column].str.split('/', n=1).str[0]  # Keep only the part before "/"

# For the "Batch" column, add "19" only if the cell value is less than 3 digits
for column in ['Batch']:
    if column in df.columns:
        df[column] = df[column].apply(lambda x: '19' + str(x) if len(str(x)) < 3 else str(x))  # Add "19" if < 3 digits

# For the "Branch" column, add "19" before the value only if it's exactly 2 digits
for column in ['Branch']:
    if column in df.columns:
        df[column] = df[column].apply(lambda x: '19' + str(x) if str(x).isdigit() and len(str(x)) == 2 else str(x))

# Print the cleaned DataFrame
print(df)
print(f"Shape after cleaning: {df.shape}")

# Save the cleaned DataFrame to a new Excel file
new_file_name = "new_copy.xlsx"
with pd.ExcelWriter(new_file_name, engine='openpyxl') as writer:
    # Write the cleaned DataFrame to a new sheet
    df.to_excel(writer, sheet_name='CleanedData', index=False)

print(f"Cleaned data saved to {new_file_name}")