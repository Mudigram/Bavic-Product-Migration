import pandas as pd
from openai import OpenAI
import time

# Read the CSV file containing product data
# Load the CSV file
df = pd.read_csv('Updated_Image_URLs.csv')

# Function to generate description using OpenAI
def generate_descriptions(name, category, tags):
    prompt = f"""You are a product description writer. Write a compelling short description (max 30 words) and a detailed product description for the following:

Product Name: {name}
Category: {category}
Tags: {tags}

Format:
Short: <short description>
Full: <full description>
"""

    try:
        response = client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=300
        )
        content = response.choices[0].message.content
        short = content.split("Short:")[1].split("Full:")[0].strip()
        full = content.split("Full:")[1].strip()
        return short, full
    except Exception as e:
        print("Error:", e)
        return "", ""

# Generate and update the CSV
for i, row in df.iterrows():
    name = row.get('Name', '')
    category = row.get('Categories', '')
    tags = row.get('Tags', '')

    short_desc, full_desc = generate_descriptions(name, category, tags)
    df.at[i, 'Short description'] = short_desc
    df.at[i, 'Description'] = full_desc

    print(f"Done with product {i+1}/{len(df)}: {name}")
    time.sleep(1.2)  # Respect API rate limits

# Save the updated CSV
df.to_csv('Final_Product_File_with_Descriptions.csv', index=False)
print("All done! Updated CSV saved as 'Final_Product_File_with_Descriptions.csv'")
