import os
from PIL import Image

def is_png(file_path):
    """Check if a file is actually a PNG based on its magic number."""
    with open(file_path, 'rb') as f:
        return f.read(8) == b'\x89PNG\r\n\x1a\n'

def convert_png_named_as_jpg_to_real_jpg(folder):
    for root, _, files in os.walk(folder):
        for file in files:
            if file.lower().endswith(".jpg"):
                file_path = os.path.join(root, file)

                if is_png(file_path):
                    print(f"Converting (was PNG): {file_path}")
                    try:
                        with Image.open(file_path) as img:
                            rgb_image = img.convert("RGB")
                            rgb_image.save(file_path, "JPEG")
                    except Exception as e:
                        print(f"Failed to convert {file_path}: {e}")

# Set path to the 'Renamed' folder
renamed_folder = r"C:\Users\Msi\Desktop\Basic Sewing\Renamed"
convert_png_named_as_jpg_to_real_jpg(renamed_folder)
print("Conversion complete.")
