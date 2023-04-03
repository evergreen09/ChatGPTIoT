import requests
import csv
from bs4 import BeautifulSoup

api_key = '0P1GMF6NdTmYEmAyxDPGH1SwvOpYv2QJ'
url = 'https://api.nytimes.com/svc/topstories/v2/home.json?api-key=' + api_key

response = requests.get(url)
data = response.json()

# Function to scrape the article text using Beautiful Soup
def get_article_text(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p', class_='css-axufdj evys1bk0')
        return ' '.join([p.text for p in paragraphs])
    except:
        return 'Error retrieving article'

# Prepare the CSV file
with open('nyt_top_stories_with_text.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['title', 'url', 'section', 'published_date', 'article_text']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    # Write the articles
    for article in data['results']:
        article_text = get_article_text(article['url'])
        writer.writerow({
            'title': article['title'],
            'url': article['url'],
            'section': article['section'],
            'published_date': article['published_date'],
            'article_text': article_text
        })

print('output.csv')
