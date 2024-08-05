import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'asm1.csv'
df = pd.read_csv(file_path)

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

# Visualization 4: Line chart for number of sales over time
plt.figure(figsize=(10, 6))
df_sorted = df.sort_values('SaleDate')

# Grouping by date and summing the quantity sold on each date
sales_over_time = df_sorted.groupby('SaleDate')['Quantity'].sum()

# Plotting the line chart
plt.plot(sales_over_time.index, sales_over_time.values, marker='o')
plt.title('Number of Sales Over Time')
plt.xlabel('Sale Date')
plt.ylabel('Number of Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
