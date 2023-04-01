import os
import openai
import csv

csv_file_path = 'output.csv'  # Replace with the actual file path

# Read the CSV data and store it as a string
with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        csv_data_string = row[0]  # Assuming the data is in the first column
        break  # We only need the first row's data

print("CSV data as string:", csv_data_string)


openai.api_key = ''

response = openai.Completion.create(
  model="text-davinci-003",
  prompt= csv_data_string + "\n\nSummarize this with concise language and a clearer structure",
  max_tokens=1300,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

print(response)