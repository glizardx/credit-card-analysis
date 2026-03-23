"""
Exploratory Analysis — Default of Credit Card Clients
Dataset: UCI Machine Learning Repository (Yeh & Lien, 2009)
"""

import pandas as pd

# Load dataset
df = pd.read_excel('data/default_of_credit_card_clients.xls', header=1)
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
print(f"Null values: {df.isnull().sum().sum()}\n")

# Columns selected for analysis
columns = [
    'LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE',
    'PAY_0', 'PAY_2', 'PAY_3', 'BILL_AMT1', 'PAY_AMT1',
    'default payment next month'
]

for col in columns:
    s = df[col]
    print(f"--- {col} ---")
    print(f"Distinct values: {s.nunique()}")
    print(f"Min: {s.min()}, Max: {s.max()}, Mode: {s.mode()[0]}")
    print(f"Mean: {s.mean():.2f}, Std: {s.std():.2f}")
    print(f"Median: {s.median():.2f}")
    print(f"Nulls: {s.isnull().sum()}\n")

# Target distribution
print("--- Target Distribution ---")
print(df['default payment next month'].value_counts())
print(f"Default rate: {df['default payment next month'].mean()*100:.1f}%")

# Export clean CSV (removes Excel currency formatting)
df.to_csv('data/default_credit_card_clients.csv', index=False)
print("\nClean CSV exported to data/")
