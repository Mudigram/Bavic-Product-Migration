import pandas as pd
import re

# Load the CSV file
df = pd.read_csv("Old_Product_Details.csv")

# Function to extract YouTube link
def extract_youtube_link(text):
    if pd.isna(text):
        return None
    match = re.search(r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/[^\s"\']+', text)
    return match.group(0) if match else None

# Apply to the Description column (or adjust if the column name differs)
df['YouTube Link'] = df['Description'].apply(extract_youtube_link)

# Filter to only rows with YouTube links
result_df = df[df['YouTube Link'].notna()][['Name', 'YouTube Link']]

# Show result
print(result_df)

# Optional: Save to CSV
result_df.to_csv("YouTube_Links_And_Product_Names.csv", index=False)
print("YouTube links and product names saved to 'YouTube_Links_And_Product_Names.csv'.")
# Optional: Save to Excel