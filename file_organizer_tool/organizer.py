import os
import shutil
from file_types import EXTENSIONS

def create_category_folders(directory):
    """Create folders for each category if they don't exist"""
    for category in EXTENSIONS.keys():
        category_path = os.path.join(directory, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

def get_category(file_extension):
    """Determine the category of a file based on its extension"""
    file_extension = file_extension.lower()
    for category, extensions in EXTENSIONS.items():
        if file_extension in extensions:
            return category
    return "others"

def organize_directory(directory):
    """Organize files in the given directory into category-based folders"""
    create_category_folders(directory)

    # Get all files in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        # Skip if it's a directory or the file doesn't exist
        if os.path.isdir(filepath):
            continue

        # Get file extension
        file_extension = os.path.splitext(filename)[1]
        if not file_extension:
            continue

        # Determine category and move file
        category = get_category(file_extension)
        destination = os.path.join(directory, category, filename)

        # Handle duplicate filenames
        counter = 1
        while os.path.exists(destination):
            name, ext = os.path.splitext(filename)
            new_name = f"{name}_{counter}{ext}"
            destination = os.path.join(directory, category, new_name)
            counter += 1

        # Move the file
        shutil.move(filepath, destination)
