import csv
import openai
import json

# Load your API key from an environment variable or secret management service
openai.api_key = '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'
csv_file_path = 'output.csv'  # Replace with the actual file path


with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        csv_data_string = row[0]  # Assuming the data is in the first column
        break  # We only need the first row's data

print("CSV data as string:", csv_data_string)



response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant that summarizes news article in 200~400 words for busy Traders."},
        {"role": "user", "content": csv_data_string + "\n\nSummarize this with concise language and a clearer structure"}
    ]
)

print(type(response))
my_dict = response.to_dict()
my_json_str = json.dumps(my_dict)

parsed_data = json.loads(my_json_str)
content = parsed_data['choices'][0]['message']['content']
print(content)
