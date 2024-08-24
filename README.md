Solution for problem statement :

Step 1: Data Ingestion
1.1 Fetch Data from Flat Files (CSV Files)
Python Script for Reading CSV File:

import pandas as pd

# Read the sales_data CSV file
sales_data = pd.read_csv('sales_data.csv')
print(sales_data.head())
1.2 Fetch Data from External API (Exchange Rates)
Python Script for Fetching Data from External API:

import requests
import pandas as pd

# API endpoint
url = 'https://example.com/api/exchange_rates'
# Send a GET request to the API
response = requests.get(url)
data = response.json()
exchange_rates = pd.DataFrame(data)
print(exchange_rates.head())
1.3 Fetch Data from Internal API (Customer Demographics)
Python Script for Fetching Data from Internal API:

import requests
import pandas as pd

# API endpoint
url = 'https://example.com/api/customer_data'
headers = {'Authorization': 'Bearer YOUR_TOKEN_HERE'}
response = requests.get(url, headers=headers)
data = response.json()
customer_data = pd.DataFrame(data)
print(customer_data.head())
1.4 Fetch Data from Database
Python Script for Fetching Data from Azure SQL Database:

import pyodbc
import pandas as pd

# Connection parameters
conn_str = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=your_server.database.windows.net;DATABASE=your_db;UID=your_user;PWD=your_password'
conn = pyodbc.connect(conn_str)

# Query to fetch data from products table
query = "SELECT * FROM products;"
products_df = pd.read_sql(query, conn)

# Query to fetch data from transactions table
query = "SELECT * FROM transactions;"
transactions_df = pd.read_sql(query, conn)

conn.close()

print(products_df.head())
print(transactions_df.head())
Step 2: Standardization
2.1 Design Data Model
Design a unified schema combining data from all sources:
•	Sales Data
o	Transaction_ID (int)
o	Product_ID (int)
o	Quantity (int)
o	Price (float)
o	Transaction_Date (date)
•	Exchange Rates
o	Currency_Code (string)
o	Exchange_Rate (float)
o	Date (date)
•	Customer Data
o	Customer_ID (int)
o	Customer_Name (string)
o	Age (int)
o	Gender (string)
o	Location (string)
o	Date_Joined (date)
•	Products Table
o	Product_ID (int) - Primary Key
o	Product_Name (string)
o	Category (string)
o	Price (float)
o	Stock_Available (int)
•	Transactions Table
o	Transaction_ID (int) - Primary Key
o	Customer_ID (int) - Foreign Key
o	Product_ID (int) - Foreign Key
o	Quantity (int)
o	Transaction_Date (date)
o	Total_Amount (float)

2.2 Implement Transformation Logic
Python Script for Transformation and Merging Data:

# Merge dataframes based on common keys
merged_data = sales_data.merge(products_df, on='Product_ID')
merged_data = merged_data.merge(exchange_rates, left_on='Currency_Code', right_on='Currency_Code')
merged_data['Total_Amount'] = merged_data['Quantity'] * merged_data['Price'] * merged_data['Exchange_Rate']
merged_data = merged_data.merge(customer_data, left_on='Customer_ID', right_on='Customer_ID')

# Save the standardized data
merged_data.to_csv('standardized_data.csv', index=False)
Step 3: Data Preprocessing Pipeline
3.1 Handle Missing Data, Duplicate Records, Inconsistent Entries
Python Script for Preprocessing Data:

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
Step 4: Cloud Architecture on Azure
4.1 Design Cloud-Based Architecture
Architecture Components:
1.	Data Ingestion:
o	Azure Functions: Serverless compute service to fetch and process data.
o	Azure Blob Storage: Store raw and processed data files.
2.	Data Processing:
o	Azure Data Factory (ADF): ETL service to orchestrate and automate data processing.
o	Azure Databricks: For scalable data processing and transformations.
3.	Database:
o	Azure SQL Database: Managed relational database service for structured data storage.
4.	APIs:
o	Azure API Management: Manage and expose APIs.
o	Azure Functions: Handle API requests and responses.
5.	Data Storage:
o	Azure Blob Storage: Store processed data and backups.
6.	Data Visualization:
o	Power BI: For BI and data visualization.
Azure Architecture Diagram:

[External API] ---> [Azure Functions] ---> [Azure Blob Storage: Raw Data] ---> [Azure Data Factory] ---> [Azure SQL Database]
                                      |
                                      V
                            [Azure Databricks: Data Processing]
4.2 Deployment Steps
1.	Create and deploy Azure Functions:
o	Set up Azure Functions to fetch data from APIs and store it in Azure Blob Storage.
o	Implement function triggers to handle data ingestion.
2.	Set up Azure Data Factory:
o	Design and deploy pipelines to orchestrate data movement and transformation.
o	Use ADF to move data from Blob Storage to Azure SQL Database.
3.	Deploy Azure Databricks:
o	Set up Databricks clusters for processing and transformation of data.
o	Write notebooks to handle data cleaning, feature engineering, and transformation.
4.	Configure Azure SQL Database:
o	Create a SQL Database in Azure and design tables to store standardized and processed data.
5.	Expose APIs using Azure API Management:
o	Create and manage APIs using Azure API Management.
o	Use Azure Functions to handle API requests.
6.	Set up Power BI for Visualization:
o	Connect Power BI to Azure SQL Database for data visualization and reporting.

![image](https://github.com/user-attachments/assets/1f660bd9-bb98-42e7-93f9-e5b25c807e4d)

