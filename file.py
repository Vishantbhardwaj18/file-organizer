import os
import shutil

# Define the directory to organize
directory_to_organize = "C:/path/to/your/directory"

# Define the types of files and their corresponding folders
file_types = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".doc", ".csv"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".tif", ".tiff"],
    "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov", ".wmv", ".webm"],
    "Music": [".mp3", ".wav", ".aac", ".flac", ".m4a", ".wma"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Code": [".py", ".java", ".c", ".cpp", ".html", ".css", ".js"],
    "Executables": [".exe", ".bat", ".msi", ".sh"],
    "Others": []  # If any files don't match the above types
}

def organize_files(directory):
    # Iterate through each file in the directory
    for filename in os.listdir(directory):
        # Get the file extension
        file_extension = os.path.splitext(filename)[1].lower()
        
        # Skip if it's a directory
        if os.path.isdir(os.path.join(directory, filename)):
            continue

        # Determine the category for the file
        moved = False
        for category, extensions in file_types.items():
            if file_extension in extensions:
                category_folder = os.path.join(directory, category)
                # Create the folder if it doesn't exist
                if not os.path.exists(category_folder):
                    os.makedirs(category_folder)
                # Move the file into the corresponding folder
                shutil.move(os.path.join(directory, filename), os.path.join(category_folder, filename))
                moved = True
                break
        
        # If the file doesn't match any type, move it to "Others"
        if not moved:
            other_folder = os.path.join(directory, "Others")
            if not os.path.exists(other_folder):
                os.makedirs(other_folder)
            shutil.move(os.path.join(directory, filename), os.path.join(other_folder, filename))

def main():
    print("Organizing files...")
    organize_files(directory_to_organize)
    print("Files organized successfully!")

if __name__ == "__main__":
    main()
