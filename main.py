import os
import shutil

# Get the Downloads folder path for the current user
from pathlib import Path
downloads_path = str(Path.home() / "Downloads")

# Define file type categories and corresponding extensions
file_categories = {
    'exe files': ['.exe'],
    'img files': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'txt files': ['.txt', '.pdf', '.docx'],
    'iso files': ['.iso'],
    'jar files': ['.jar'],
    'zip folders': ['.zip', '.rar', '.7z']
}

# Create folders if they don't exist
for folder in file_categories:
    folder_path = os.path.join(downloads_path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created folder: {folder_path}")

# Move matching files into corresponding folders
for filename in os.listdir(downloads_path):
    file_path = os.path.join(downloads_path, filename)
    if os.path.isfile(file_path):
        _, ext = os.path.splitext(filename.lower())
        for folder, extensions in file_categories.items():
            if ext in extensions:
                dest_path = os.path.join(downloads_path, folder, filename)
                if not os.path.exists(dest_path):
                    shutil.move(file_path, dest_path)
                    print(f"Moved {filename} → {folder}")
                break
