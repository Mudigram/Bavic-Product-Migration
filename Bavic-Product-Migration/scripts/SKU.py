import pandas as pd

# Load your cleaned products file
products = pd.read_csv('cleaned_products_withopenai.csv')

# Starting SKU number
start_number = 212  # because you want BSA-000211-C

# Function to generate SKU
def generate_sku(index):
    sku_number = start_number + index
    return f"BSA-{sku_number:05d}-C"  # 5 digits with leading zeros

# Apply the function to create new SKUs
products['SKU'] = [generate_sku(i) for i in range(len(products))]

# Save the updated file
products.to_csv('cleaned_products_with_sku2.csv', index=False)

print("✅ Updated SKUs and saved as cleaned_products_with_sku2.csv")
