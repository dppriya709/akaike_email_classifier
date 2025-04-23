import pandas as pd

# Load the dataset
df = pd.read_csv("data/combined_emails_with_natural_pii.csv")  # Change filename if needed

# View the first few rows
print(df.head())

# Check columns
print(df.columns)
