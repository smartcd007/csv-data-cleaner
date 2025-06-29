import pandas as pd

# Load CSV
df = pd.read_csv("data/sample_data.csv")
print("Original Data:\n", df)

# Step 1: Ensure Date is a string and clean weird dash characters
df['Date'] = df['Date'].astype(str)  # Make sure all values are strings

# Replace en dash (–), em dash (—), and slashes (if needed) with "-"
df['Date'] = df['Date'].str.replace('–', '-', regex=False)
df['Date'] = df['Date'].str.replace('—', '-', regex=False)
df['Date'] = df['Date'].str.replace('/', '-', regex=False)

print("\nCleaned Date column:\n", df['Date'])

# Step 2: Drop duplicates
df = df.drop_duplicates()

# Step 3: Drop rows with missing values
df = df.dropna()

# Step 4: Convert to datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Step 5: Drop rows with invalid Date
df = df.dropna(subset=['Date'])

# Step 6: Save cleaned file
df.to_csv("data/cleaned_data.csv", index=False)
print("\nCleaned data saved to cleaned_data.csv:\n", df)



