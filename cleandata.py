import pandas as pd

# Load the DataFrame from an Excel file with error handling
try:
    df = pd.read_excel("vissco.xlsx")  # Load your original data
except Exception as e:
    print(f"Error loading the Excel file: {e}")
    exit()
# Print initial shape and any missing values
print("Initial DataFrame Shape:", df.shape)
print("Missing Values:\n", df.isnull().sum())

# Remove duplicates
df_cleaned = df.drop_duplicates()
# Print shape after removing duplicates
print("Shape after removing duplicates:", df_cleaned.shape)

# Check if cleaned DataFrame is not empty
if not df_cleaned.empty:
    # Save cleaned DataFrame to a new sheet in a new Excel file
    output_file = 'vissco_cleaned_data.xlsx'  # Specify the output file name
    with pd.ExcelWriter(output_file, engine='openpyxl', mode='w') as writer:
        df_cleaned.to_excel(writer, index=False, sheet_name='Cleaned Data')  # Save to a new sheet

    print(f"Cleaned data successfully saved to {output_file}")
else:
    print("Cleaned DataFrame is empty. No data to save.")
