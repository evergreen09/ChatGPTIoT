import csv
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = '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'

with open('output.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = list(reader)
    text = '\n'.join([','.join(row) for row in rows])




response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)

print(response)