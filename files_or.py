import os
import shutil

def organize_files(source_dir:str):
    # Check if the source directory exists.
    if not os.path.exists(source_dir):
        print(f"{source_dir} does not exist.")

    # Create a new a directory to store organized files (if not already exists).
    org_dir = os.path.join(source_dir, "Sorted")
    os.makedirs(org_dir, exist_ok=True)

    # Iterate over files in the source directory.
    files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]

    for file in files:
        # Get the file extension.
        _, ext = os.path.splitext(file)

        # Remove the dot from the file extension.
        ext = ext.lstrip(".")

        # Create a directory for the file extension (if not already exists).
        ext_dir = os.path.join(org_dir, ext)
        os.makedirs(ext_dir, exist_ok=True)

        # Move the file to its corresponding directory.
        source_path = os.path.join(source_dir, file)
        destination_path = os.path.join(ext_dir, file)
        shutil.move(source_path, destination_path)
        print(f"Moved {file} -> {ext}/{file}")

if __name__ == "__main__":
    src_dir = input("Enter the source directory path: ")
    organize_files(src_dir)