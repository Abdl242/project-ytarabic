
import os
import shutil

def save_to_local_icloud(file):

    # Define the source and destination paths
    source_file = file  # Replace with the path to your .md file
    icloud_path = os.path.expanduser("~/Library/Mobile Documents/iCloud~md~obsidian/Documents/brain/")
    destination_file = os.path.join(icloud_path, os.path.basename(source_file))

    # Ensure the iCloud folder exists
    if not os.path.exists(icloud_path):
        os.makedirs(icloud_path)

    # Copy the file to the iCloud folder
    shutil.copy(source_file, destination_file)

    print(f"Markdown file copied to: {destination_file}")
