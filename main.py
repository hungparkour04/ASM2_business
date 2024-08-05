import pandas as pd

# Load the CSV file
file_path = 'asm1.csv'
df = pd.read_csv(file_path)

# Check for missing values
missing_values = df.isnull().sum()
print(missing_values)

# Handle missing values
df['Quantity'].fillna(0, inplace=True)
df['SalesRepID'].fillna('Unknown', inplace=True)
df['OrderStatus'].fillna('Unknown', inplace=True)

# Convert SaleDate to datetime format
df['SaleDate'] = pd.to_datetime(df['SaleDate'], format='%m/%d/%Y')

# Ensure numerical columns are correctly typed
df['Quantity'] = df['Quantity'].astype(int)
df['TotalAmount'] = df['TotalAmount'].astype(float)
df['DiscountApplied'] = df['DiscountApplied'].astype(float)

# Ensure consistency in OrderStatus
df['OrderStatus'] = df['OrderStatus'].str.strip().str.title()

# Remove any duplicate rows if they exist
df.drop_duplicates(inplace=True)

# Reset the index of the DataFrame
df.reset_index(drop=True, inplace=True)

# Display the cleaned DataFrame
print(df)

# Save the cleaned DataFrame to a new CSV file
new_file_path = 'cleaned_asm1.csv'
df.to_csv(new_file_path, index=False)
