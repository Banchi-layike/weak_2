import pandas as pd

# Load data
data = pd.read_csv('data.csv')

# Display initial data
print("Initial Data:")
print(data.head())

# Drop missing values
data_cleaned = data.dropna()

# Rename columns
data_cleaned.rename(columns={'old_name': 'new_name'}, inplace=True)

# Filter data (e.g., keep only rows where 'age' > 18)
data_filtered = data_cleaned[data_cleaned['age'] > 18]

# Create a new column (e.g., full name)
data_filtered['full_name'] = data_filtered['first_name'] + ' ' + data_filtered['last_name']

# Display transformed data
print("Transformed Data:")
print(data_filtered.head())

# Save transformed data to a new CSV
data_filtered.to_csv('transformed_data.csv', index=False)
import pandas as pd

# Load data
data = pd.read_csv('sales_data.csv')

# Group by a column and calculate the sum
grouped_data = data.groupby('product')['sales'].sum().reset_index()

# Sort by sales
sorted_data = grouped_data.sort_values(by='sales', ascending=False)

# Display aggregated data
print("Aggregated Data:")
print(sorted_data)

# Save aggregated data to a new CSV
sorted_data.to_csv('aggregated_sales_data.csv', index=False)
import pandas as pd
import json

# Load JSON data
with open('data.json', 'r') as file:
    data = json.load(file)

# Convert to DataFrame
df = pd.DataFrame(data)

# Perform transformations (e.g., filter, group)
df_filtered = df[df['age'] > 21]

# Save transformed data back to JSON
df_filtered.to_json('filtered_data.json', orient='records', lines=True)
import pandas as pd
import json

# Load JSON data
with open('data.json', 'r') as file:
    data = json.load(file)

# Convert to DataFrame
df = pd.DataFrame(data)

# Perform transformations (e.g., filter, group)
df_filtered = df[df['age'] > 21]

# Save transformed data back to JSON
df_filtered.to_json('filtered_data.json', orient='records', lines=True)
