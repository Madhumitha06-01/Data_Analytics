import pandas as pd

# Read the Excel file
df = pd.read_excel("vissco.xlsx")
duplicates = df.duplicated().sum()
print(duplicates)
df.drop_duplicates(inplace=True)
# Print shape after removing duplicates
data = df.fillna(method ='bfill')
# console the data 
print(data)      
# Check if DataFrame is not empty before saving
if not df.empty:
    # Save the cleaned DataFrame to a new Excel file
    output_file = 'vissco_cleaned_data.xlsx'  # Specify the output file name
    df.to_excel(output_file, index=False, sheet_name='Cleaned Data')  # You can specify a sheet name

    print(f"Data successfully saved to {output_file}")
else:
    print("DataFrame is empty. No data to save.")
