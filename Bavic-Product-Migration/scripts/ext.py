import pandas as pd
import re

# === CONFIG ===
old_csv_path = "Old_Product_Details.csv"  # Path to old product CSV
description_column = "Description"  # Change this if your column name is different
output_csv = "product_youtube_links.csv"  # Output file

# === Function to Extract YouTube Links ===
def extract_youtube_link(text):
    if pd.isna(text):
        return None
    match = re.search(r'(https?://(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)[\w\-]+)', text)
    return match.group(1) if match else None

# === Load CSV and Extract Links ===
df = pd.read_csv(old_csv_path)
df['YouTube Link'] = df[description_column].apply(extract_youtube_link)

# Keep only rows with a YouTube link
df_with_links = df[['Description', 'YouTube Link']].dropna()

# === Save Result ===
df_with_links.to_csv(output_csv, index=False)
print(f"✅ Extracted YouTube links saved to '{output_csv}'")
