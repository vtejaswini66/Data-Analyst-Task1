import pandas as pd
df = pd.read_csv('raw_dataset.csv')
df = df.fillna(method='ffill')
df = df.drop_duplicates()
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].astype(str).str.strip().str.lower()
df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]
df.to_csv('cleaned_dataset.csv', index=False)

print('Data cleaning completed')
