import pandas as pd
import openai
import time
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key="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")  # Replace with your actual API key

# Load CSV
df = pd.read_csv("Old_Product_Details.csv")

# Add a new column if it doesn't exist
if 'Refined Description' not in df.columns:
    df['Refined Description'] = ""

# Filter rows that need processing
to_process = df[df['Refined Description'].isna() | (df['Refined Description'] == "")]

def refine_description(text):
    prompt = f"""
Refine the following product description to improve clarity, grammar, and flow without changing the number of words significantly or altering the format:

Original:
{text}

Refined:
"""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=1000
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("Error:", e)
        return text

# Process in batches of 50
batch_size = 50
for start in range(0, len(to_process), batch_size):
    end = start + batch_size
    print(f"Processing rows {start} to {end - 1}...")

    batch = to_process.iloc[start:end]
    for idx in batch.index:
        original = df.at[idx, 'Description']
        refined = refine_description(original)
        df.at[idx, 'Refined Description'] = refined
        time.sleep(1)  # Be kind to the API

    df.to_csv("Refined_Descriptions.csv", index=False)
    print(f"✅ Saved batch {start // batch_size + 1} to 'Refined_Descriptions.csv'")

print("🎉 All done!")
