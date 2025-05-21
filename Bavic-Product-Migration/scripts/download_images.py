# download_images.py

import os
import requests

# Folder to save downloaded images
output_folder = "downloaded_images"
os.makedirs(output_folder, exist_ok=True)

# Read image URLs from the text file
with open("old_image_links.txt", "r") as f:
    urls = [line.strip() for line in f if line.strip()]

for i, url in enumerate(urls, start=1):
    try:
        file_ext = url.split('.')[-1].split('?')[0].lower()
        filename = f"image_{i:04d}.{file_ext}"
        filepath = os.path.join(output_folder, filename)

        # Download image
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            with open(filepath, "wb") as img_file:
                img_file.write(response.content)
            print(f"✅ Downloaded: {filename}")
        else:
            print(f"❌ Failed to download {url} - Status code: {response.status_code}")
    except Exception as e:
        print(f"⚠️ Error downloading {url} - {e}")

print("🎉 All downloads finished.")
# Note: This script assumes that the URLs in old_image_links.txt are valid and accessible.