import pandas as pd

# Load both files
file_with_links = pd.read_csv("YouTube_Links_And_Product_Names.csv")  # File A
full_product_file = pd.read_csv("New_Product_Details.csv")  # File B

# Get just the list of product names that have YouTube links
products_with_links = set(file_with_links['Name'].str.strip().str.lower())

# Remove products from File B whose 'Title' is in File A
filtered_products = full_product_file[~full_product_file['Name'].str.strip().str.lower().isin(products_with_links)]

# Save the result
filtered_products.to_csv("Filtered_Products_Without_YT_Duplicates.csv", index=False)

print("Filtered file saved as 'Filtered_Products_Without_YT_Duplicates.csv'")
