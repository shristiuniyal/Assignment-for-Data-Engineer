# Load the standardized data
data = pd.read_csv('standardized_data.csv')

# Drop duplicates
data = data.drop_duplicates()

# Fill missing values
data['Price'] = data['Price'].fillna(data['Price'].median())
data['Quantity'] = data['Quantity'].fillna(data['Quantity'].median())

# Handle inconsistent data (e.g., negative prices)
data = data[data['Price'] >= 0]

# Convert categorical variables to dummy variables
data = pd.get_dummies(data, columns=['Gender', 'Category'])

# Save the cleaned data
data.to_csv('preprocessed_data.csv', index=False)

