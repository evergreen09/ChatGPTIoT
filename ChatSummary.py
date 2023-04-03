import csv
import openai
import json
import os

# Load your API key from an environment variable or secret management service
openai.api_key = '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'
json_file_path = 'article.json'  # Replace with the actual file path
datasets_file_path = 'datasets.json'

# Read the article data from the JSON file
with open(json_file_path, 'r', encoding='utf-8') as json_file:
    articles = json.load(json_file)

# Process each article
for article in articles:
    csv_data_string = list(article.values())[0]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes news article in 200~400 words for busy Traders."},
            {"role": "user", "content": csv_data_string + "\n\nSummarize this with concise language and a clearer structure"}
        ]
    )

    my_dict = response.to_dict()
    my_json_str = json.dumps(my_dict)

    parsed_data = json.loads(my_json_str)
    content = parsed_data['choices'][0]['message']['content']

    # Check if the datasets.json file exists, otherwise create an empty file with an empty list
    if not os.path.exists(datasets_file_path):
        with open(datasets_file_path, 'w') as json_file:
            json.dump([], json_file)

    # Load the existing datasets from the JSON file
    try:
        with open(datasets_file_path, 'r') as json_file:
            datasets = json.load(json_file)
    except json.JSONDecodeError:
        datasets = []

    # Add the new dataset
    datasets.append({'prompt': csv_data_string, 'completion': content})

    # Write the updated datasets to the JSON file
    with open(datasets_file_path, 'w') as json_file:
        json.dump(datasets, json_file)
