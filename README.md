# Bavic-Product-Migration
Python scripts for cleaning, refining, and migrating 800+ products to a new eCommerce store on WordPress

# 🧵 Product Migration with Python

This repo contains Python scripts I built to help a client migrate 800+ products to a new eCommerce store (bavicsewingaccessories.com.ng). The original data had broken image references, missing YouTube links, and inconsistent descriptions.

I used GPT-4 + Python to:
- Scan and fix image file extensions
- Extract embedded YouTube links from old descriptions
- Refine product descriptions without losing structure or word count
- Filter and merge clean product data for CSV upload

## 🔧 Tools Used
- Python 3.x
- pandas
- OpenAI API
- Regex
- CSV handling

## 📁 Folder Structure
- `data/`: Sample input and output CSVs
- `scripts/`: Modular scripts used during cleanup
- `images/`: Image Files I worked with from start to finish

## 🚀 How to Run
```bash
pip install -r requirements.txt
python scripts/extract_youtube_links.py
python scripts/refine_descriptions.py

# You’ll need an OpenAI API key to run the GPT-powered script.
