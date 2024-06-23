import pandas as pd
import numpy as np

# Data Loading
# Load data from CSV
df = pd.read_csv('sample_data.csv')

# For demonstration purposes, creating a sample Excel file
df.to_excel('sample_data.xlsx', index=False)
df_excel = pd.read_excel('sample_data.xlsx')

# Creating a sample SQL database
from sqlalchemy import create_engine
engine = create_engine('sqlite:///sample_data.db')
df.to_sql('sample_table', engine, if_exists='replace', index=False)
df_sql = pd.read_sql('SELECT * FROM sample_table', engine)

# Data Inspection
print(df.head())  # Display first 5 rows
print(df.tail())  # Display last 5 rows
print(df.info())  # Summary of the dataframe
print(df.describe())  # Descriptive statistics

# Data Cleaning
df.dropna(subset=['A'], inplace=True)  # Drop rows with missing values in column 'A'
df['A']=df['A'].fillna(df['A'].mean())  # Fill missing values with mean
#df['C'].replace('X', 'W', inplace=True)  # Replace values in column 'C'
df['C'] = df['C'].replace('X','W')
df.drop_duplicates(subset=['A'], keep='first', inplace=True)  # Drop duplicate rows

# Data Transformation
df['new_column'] = df['A'] + df['B']  # Create new column as sum of two columns
df['Date'] = pd.to_datetime(df['Date'])  # Convert column to datetime
df.set_index('Date', inplace=True)  # Set column as index
df.reset_index(inplace=True)  # Reset index

# Data Selection
value = 50
df_filtered = df[df['A'] > value]  # Filter rows based on condition
df_selected = df[['A', 'B', 'C']]  # Select specific columns
new_value = 75
df.loc[df['A'] > value, 'A'] = new_value  # Conditional assignment

# Grouping and Aggregation
df_grouped = df.groupby('C').agg({'A': 'mean', 'B': 'sum'})  # Group by and aggregate
df_pivot = df.pivot_table(index='A', columns='C', values='B', aggfunc='mean')  # Pivot table

# For demonstration purposes, creating additional dataframes
df1 = df.copy()
df2 = df.copy()

# Merging and Joining
df_merged = pd.merge(df1, df2, on='A', how='inner', suffixes=('_left', '_right'))  # Merge dataframes
df_joined = df1.join(df2.set_index('A'), on='A', rsuffix='_joined')  # Join dataframes

# Data Analysis
print(df['C'].value_counts())  # Count unique values
print(df['C'].unique())  # Get unique values
print("HERE")
print(df.describe())
#print(df2.corr())  # Correlation matrix
df['rolling_mean'] = df['A'].rolling(window=7).mean()  # Rolling window calculations

# Advanced Data Manipulations
df['rank'] = df['A'].rank()  # Rank values
df['quantile'] = pd.qcut(df['A'], q=4, labels=False, duplicates='drop')  # Quantile-based discretization
df['category'] = df['C'].astype('category')  # Convert column to category dtype

# Time Series Analysis
df.set_index('Date', inplace=True)  # Ensure Date is index for resampling
df['resample'] = df['A'].resample('ME').sum()  # Resample time series data

# Visualization (requires matplotlib and seaborn)
import matplotlib.pyplot as plt
import seaborn as sns

# Basic Plot
df['A'].plot(kind='line')
plt.show()

# Histogram
df['A'].hist(bins=30)
plt.show()

# Box Plot
sns.boxplot(x='C', y='A', data=df)
plt.show()

# Scatter Plot
sns.scatterplot(x='A', y='B', data=df)
plt.show()

# Pair Plot
sns.pairplot(df[['A', 'B', 'D']])
plt.show()

# Save Data
df.to_csv('cleaned_data.csv', index=False)
df.to_excel('cleaned_data.xlsx', index=False)
df.to_sql('cleaned_data_table', engine, if_exists='replace', index=False)

print("Pandas comprehensive script executed successfully.")
