import os
import shutil


# Defines a mapping from file extensions to their corresponding target folder names.
# This dictionary is used to categorize files based on their type.
EXTENSION_TO_FOLDER_MAP = {
    # Images
    ".jpg": "Images", ".jpeg": "Images", ".png": "Images", ".gif": "Images", ".bmp": "Images", ".tiff": "Images", ".webp": "Images",
    # Documents
    ".txt": "Documents", ".pdf": "Documents", ".doc": "Documents", ".docx": "Documents", ".odt": "Documents", ".rtf": "Documents",
    # Archives
    ".zip": "Archives", ".tar": "Archives", ".gz": "Archives", ".rar": "Archives", ".7z": "Archives",
    # Audio
    ".mp3": "Audio", ".wav": "Audio", ".aac": "Audio", ".flac": "Audio",
    # Videos
    ".mp4": "Videos", ".mov": "Videos", ".avi": "Videos", ".mkv": "Videos", ".wmv": "Videos",
    # Scripts
    ".py": "Scripts", ".js": "Scripts", ".sh": "Scripts", ".bat": "Scripts",
    # Spreadsheets/Data
    ".csv": "Data", ".xls": "Data", ".xlsx": "Data",
    # Presentations
    ".ppt": "Presentations", ".pptx": "Presentations",
}

# Specifies the default folder name for files whose extensions are not found in EXTENSION_TO_FOLDER_MAP.
DEFAULT_TARGET_FOLDER = "Others"

# Defines the name of the folder containing the files to be organized.
source_folder = "files_to_organize"


print(f"Planning organization for items in: '{source_folder}'\n")

# Main block to handle file processing and potential errors.
try:
    # Get a list of all files and directories in the source folder.
    items_in_folder = os.listdir(source_folder)
    # Check if the folder is empty.
    if not items_in_folder:
        print("The folder is empty.")
    else:
        print("File categorization plan:\n")
    # Iterate over each item found in the source folder.
    for item_name in items_in_folder:
        # Construct the full path to the item.
        full_item_path = os.path.join(source_folder, item_name)
        # Check if the current item is a file (not a directory).
        if os.path.isfile(full_item_path):
            # Split the item name into its name part and extension part.
            file_name_part, file_extension = os.path.splitext(item_name)
            # Convert the file extension to lowercase for consistent matching.
            file_extension = file_extension.lower()
            # Check if an extension exists.
            if file_extension:
                target_folder_name = EXTENSION_TO_FOLDER_MAP.get(file_extension, DEFAULT_TARGET_FOLDER)
            else:
                target_folder_name = DEFAULT_TARGET_FOLDER

            target_folder_path = os.path.join(source_folder, target_folder_name)

            os.makedirs(target_folder_path, exist_ok=True)

            destination_file_path = os.path.join(target_folder_path, item_name)

            try:
                shutil.move(full_item_path, destination_file_path)
                print(f"Moved '{item_name}' to '{target_folder_name}'.")
            except Exception as e:
                print(f"Error moving '{item_name}': {e}")        

# Handle the case where the source folder does not exist.
except FileNotFoundError:
    print(f"The folder, '{source_folder}', does not exist.")
  
# Handle any other unexpected errors during execution.
except Exception as e:
    print(f"An unexpected error occurred: {e}")
