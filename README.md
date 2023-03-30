# Simple File Organizer

This project is a Python script that organizes files in a specified directory into subdirectories based on their file extension. It showcases file and directory manipulation using Python's standard library modules such as `os`, `shutil`, and `collections`.

## Big O Efficiency

The time complexity of the script is O(n), where n is the number of files in the directory. The script iterates through the files once to group them by extension, and then iterates through the groups to move the files to the appropriate subdirectories.

The space complexity is O(n) as well, as we store the file names in a dictionary, where the keys are the file extensions and the values are lists of file names with the corresponding extension.

## How to Run

1. Clone the repository:
    git clone https://github.com/yourusername/simple-file-organizer.git
2. Change the directory:
    cd simple-file-organizer
3. Open the `file_organizer.py` script with a text editor and set the `directory_to_organize` variable to the path of the directory you want to organize.

4. Run the script:
    python3 file_organizer.py
5. The files in the specified directory will be organized into subdirectories based on their file extension.
