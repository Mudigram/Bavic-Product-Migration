import pandas as pd

# STEP 1: Load 275 existing products
existing_products = pd.read_csv('BrandN.csv')
existing_product_names = existing_products['Name'].dropna().str.strip().str.lower()
existing_names_set = set(existing_product_names)
print(f"Loaded {len(existing_names_set)} existing product names.")

# STEP 2: Load 970 products
all_products = pd.read_csv('Final_Product_File_with_Descriptions.csv')
print(f"Loaded {len(all_products)} total products.")

# STEP 3: Filter products
all_products['Name_normalized'] = all_products['Name'].str.strip().str.lower()
new_products = all_products[~all_products['Name_normalized'].isin(existing_names_set)]
new_products = new_products.drop(columns=['Name_normalized'])
print(f"Filtered products: {len(new_products)} remaining.")

# STEP 4: Save cleaned CSV
new_products.to_csv('cleaned_products_BrandN.csv', index=False)
print("Saved the cleaned file as cleaned_products.csv")
