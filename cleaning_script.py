import pandas as pd

# Load dataset
df = pd.read_csv('raw_dataset.csv')

# Missing values
df = df.fillna(method='ffill')

# Remove duplicates
df = df.drop_duplicates()

# Standardize text
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].astype(str).str.strip().str.lower()

# Clean column names
df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]

# Save cleaned dataset
df.to_csv('cleaned_dataset.csv', index=False)

print('Data cleaning completed')
