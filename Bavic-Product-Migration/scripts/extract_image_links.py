import pandas as pd
import requests
import os

# Load the CSV file
df = pd.read_csv("Old_Product_Details.csv")

# Create output directory if not exists
os.makedirs("new_downloaded_images", exist_ok=True)

# Loop through each row
for idx, row in df.iterrows():
    image_urls = str(row['Images']).split(',')
    image_urls = [url.strip() for url in image_urls if url.strip() != '']

    # Base filename
    base_name = f"image_{idx+1:04}"

    # Download each image
    for i, url in enumerate(image_urls):
        suffix = f"-{i}" if i > 0 else ""
        filename = f"{base_name}{suffix}.jpg"
        save_path = os.path.join("new_downloaded_images", filename)

        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                with open(save_path, 'wb') as f:
                    f.write(response.content)
                print(f"Downloaded: {filename}")
            else:
                print(f"Failed to download: {url} (status {response.status_code})")
        except Exception as e:
            print(f"Error downloading {url}: {e}")
