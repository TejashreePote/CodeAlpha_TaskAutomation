import os
import shutil

source_folder = "source_folder"
destination_folder = "destination_folder"

# Create destination folder if it does not exist
os.makedirs(destination_folder, exist_ok=True)

# Move JPG files
for file in os.listdir(source_folder):
    if file.lower().endswith(".jpg"):
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)
        print(f"Moved: {file}")

print("\nAll JPG files have been moved successfully!")