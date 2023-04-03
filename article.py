import re
import json
import os
from bs4 import BeautifulSoup

def clean_string(text):
    return re.sub(r"[',]", "", text)

# Set the total number of files
number_of_files = 17  # Change this to the total number of files you have

# Process each file
for i in range(1, number_of_files + 1):
    # Read the HTML content from a file
    file_path = f'ny{i}.html'  # Replace with the actual file path
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist. Skipping.")
        continue

    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all paragraphs with the specified CSS class
    paragraphs = soup.select('p.css-at9mc1.evys1bk0')

    # Extract and clean text data from each paragraph and save it to a list
    text_data = [clean_string(paragraph.get_text(strip=True)) for paragraph in paragraphs if paragraph.get_text(strip=True)]

    

    # Save the cleaned text data to a JSON file
    json_file_path = 'article.json'  # Replace with the desired JSON file path

    # Check if the JSON file exists
    if os.path.exists(json_file_path):
        # Read the existing data from the JSON file
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
    else:
        # If the file does not exist, create an empty data list
        data = []

    # Get the next article number
    next_article_number = len(data) + 1

    # Add the new article to the data list
    combined_text_data = ' '.join(text_data)
    data.append({f'article{next_article_number}': combined_text_data})

    # Write the updated data to the JSON file
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)

    print("Current Loop: " + str(next_article_number))
