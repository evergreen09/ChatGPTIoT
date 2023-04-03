import os
import glob

def main():
    # Get the list of all html files in the working directory
    html_files = glob.glob('*.html')

    # Filter out files that start with "ny"
    html_files_to_rename = [file for file in html_files if not file.startswith("ny")]

    # Initialize the counter
    counter = 1

    # Iterate through the filtered list of html files and rename them
    for file in html_files_to_rename:
        new_file_name = f"ny{counter}.html"
        
        # Check if the new file name already exists, if so, increment the counter until it doesn't
        while os.path.exists(new_file_name):
            counter += 1
            new_file_name = f"ny{counter}.html"

        # Rename the file
        os.rename(file, new_file_name)
        
        # Increment the counter
        counter += 1

if __name__ == "__main__":
    main()
