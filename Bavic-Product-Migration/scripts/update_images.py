import pandas as pd

# === CONFIG ===
input_file = 'Formatted_Product_Details.csv'
output_file = 'Updated_Image_URLs.csv'
base_url = 'https://bavicsewingaccessories.com.ng/wp-content/uploads/2025/04/'
start_number = 1  # Start from image_0002

# === LOAD CSV ===
df = pd.read_csv(input_file)

# === UPDATE IMAGE COLUMN ===
image_counter = start_number

def format_image_urls(images):
    global image_counter
    image_count = len(str(images).split(','))
    urls = []
    for i in range(image_count):
        if i == 0:
            filename = f"image_{image_counter:04}.jpg"
        else:
            filename = f"image_{image_counter:04}-{i}.jpg"
        urls.append(f"{base_url}{filename}")
    image_counter += 1
    return ', '.join(urls)

df['Images'] = df['Images'].apply(format_image_urls)

# === SAVE NEW CSV ===
df.to_csv(output_file, index=False)
print(f"✅ CSV updated and saved as: {output_file}")
