# Project: Simple File Organizer
# This project organizes files in a specified directory into subdirectories
# based on their file extension.

import os
import shutil
from collections import defaultdict

def create_directory(directory_path, directory_name):
    """
    Creates a new directory with the given name in the specified path.

    Args:
        directory_path (str): The path where the new directory will be created.
        directory_name (str): The name of the new directory.
    """
    new_directory = os.path.join(directory_path, directory_name)
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)

def organize_files(directory_path):
    """
    Organizes the files in the specified directory by moving them into
    subdirectories based on their file extension.

    Args:
        directory_path (str): The path of the directory to be organized.
    """
    files_by_extension = defaultdict(list)

    # Group files by extension
    for filename in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, filename)):
            file_extension = os.path.splitext(filename)[1]
            files_by_extension[file_extension].append(filename)

    # Create subdirectories and move files
    for extension, files in files_by_extension.items():
        create_directory(directory_path, extension[1:])
        for file in files:
            shutil.move(
                os.path.join(directory_path, file),
                os.path.join(directory_path, extension[1:], file)
            )

if __name__ == "__main__":
    # Directory path to be organized (change this to the desired path)
    directory_to_organize = "/path/to/your/directory"

    # Organize the files in the specified directory
    organize_files(directory_to_organize)