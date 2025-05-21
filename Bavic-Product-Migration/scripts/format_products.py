import pandas as pd

# Load the product CSV
df = pd.read_csv("Old_Product_Details.csv")

# Flatten all image links into one list
all_image_urls = []

for row in df["Images"].dropna():
    for url in str(row).split(','):
        clean_url = url.strip()
        if clean_url:
            all_image_urls.append(clean_url)

# Remove duplicates
unique_image_urls = list(set(all_image_urls))

# Save them to a text file
with open("old_image_links.txt", "w") as f:
    for link in unique_image_urls:
        f.write(link + "\n")

print(f"✅ Saved {len(unique_image_urls)} unique image links.")
