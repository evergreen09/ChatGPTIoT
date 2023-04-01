import re
import csv
from bs4 import BeautifulSoup

def clean_string(text):
    return re.sub(r"[',]", "", text)

# Read the HTML content from a file
file_path = 'ny2.html'  # Replace with the actual file path
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all paragraphs with the specified CSS class
paragraphs = soup.select('p.css-at9mc1.evys1bk0')

# Extract and clean text data from each paragraph and save it to a list
text_data = [clean_string(paragraph.get_text(strip=True)) for paragraph in paragraphs if paragraph.get_text(strip=True)]

# Print the cleaned text data
print("Cleaned text data:", text_data)

# Save the cleaned text data to a CSV file
csv_file_path = 'output.csv'  # Replace with the desired CSV file path
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    combined_text_data = ' '.join(text_data)
    csv_writer.writerow([combined_text_data])

