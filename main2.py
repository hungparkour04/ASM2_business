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

# Visualization 1: Bar chart for number of sales by order status
plt.figure(figsize=(10, 6))
order_status_counts = df['OrderStatus'].value_counts()
order_status_counts.plot(kind='bar')
plt.title('Number of Sales by Order Status')
plt.xlabel('Order Status')
plt.ylabel('Number of Sales')
plt.xticks(rotation=45)
plt.show()

# Visualization 2: Pie chart for percentage of order statuses
plt.figure(figsize=(8, 8))
order_status_counts.plot(kind='pie', autopct='%1.1f%%')
plt.title('Percentage of Order Statuses')
plt.ylabel('')
plt.show()

# Visualization 3: Line chart for total sales amount over time
plt.figure(figsize=(10, 6))
df_sorted = df.sort_values('SaleDate')
plt.plot(df_sorted['SaleDate'], df_sorted['TotalAmount'], marker='o')
plt.title('Total Sales Amount Over Time')
plt.xlabel('Sale Date')
plt.ylabel('Total Sales Amount')
plt.xticks(rotation=45)
plt.show()

# Visualization 4: Bar chart for number of sales by sales representative
plt.figure(figsize=(10, 6))
sales_rep_counts = df['SalesRepID'].value_counts()
sales_rep_counts.plot(kind='bar')
plt.title('Number of Sales by Sales Representative')
plt.xlabel('Sales Representative ID')
plt.ylabel('Number of Sales')
plt.xticks(rotation=45)
plt.show()
